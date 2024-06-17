import cv2
import numpy as np

# Canny Edge Detection
def canny(image):
    grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(grey, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

# Region Of Interest
def roi(image):
    height = image.shape[0]  # ROI & Mask
    polygons = np.array([[(200, height), (1100, height), (550, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked = cv2.bitwise_and(image, mask)
    return masked

def coordinates(image, param):
    slope, intercept = param
    y1 = image.shape[0]
    y2 = int(y1 * (3 / 5))
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])

# Avg & Slope, Intercept
def avg_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        param = np.polyfit((x1, x2), (y1, y2), 1)
        slope = param[0]
        intercept = param[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    
    left_line, right_line = None, None
    
    if left_fit:
        left_fit_avg = np.average(left_fit, axis=0)
        left_line = coordinates(image, left_fit_avg)
        
    if right_fit:
        right_fit_avg = np.average(right_fit, axis=0)
        right_line = coordinates(image, right_fit_avg)
        
    return np.array([line for line in [left_line, right_line] if line is not None])

# Display Lines
def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)  
    return line_image

str = int(input("Enter 1 to pass an image or 2 to pass a video "))
if str == 1:
    # Image passing
    image = cv2.imread(r'Test/solidYellowCurve.jpg')
    temp = np.copy(image)
    canny_edge = canny(temp)
    roi_ = roi(canny_edge)
    lines = cv2.HoughLinesP(roi_, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    if lines is not None:
        avg = avg_slope_intercept(temp, lines)
        line_image = display_lines(temp, avg)
        combo_image = cv2.addWeighted(temp, 0.7, line_image, 1, 1)  # Adjust the weights to make lines darker
    else:
        combo_image = temp
    cv2.imshow('Result', combo_image)
    cv2.waitKey(0)
else:
    # Video passing
    cap = cv2.VideoCapture(r'Test/solidWhiteRight.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        temp = np.copy(frame)
        canny_edge = canny(temp)
        roi_ = roi(canny_edge)
        lines = cv2.HoughLinesP(roi_, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
        if lines is not None:
            avg = avg_slope_intercept(temp, lines)
            line_image = display_lines(temp, avg)
            combo_image = cv2.addWeighted(temp, 0.7, line_image, 1, 1)  
        else:
            combo_image = temp

        cv2.imshow('Result', combo_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

