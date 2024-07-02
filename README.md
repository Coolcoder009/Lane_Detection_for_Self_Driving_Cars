# Lane_Detection_for_Self_Driving_Cars

Lane Detection for Self-Driving Cars is a computer vision project designed to detect and visualize lane markings on road images or video streams. This project utilizes techniques like Canny edge detection, Hough transform, and polynomial fitting to identify and highlight lane lines.

## Overview
The lane detection algorithm processes input images or video frames to:

<ul>
  <li><b>Convert to Grayscale:</b> Converts the RGB image to grayscale for edge detection.</li>
  <li><b>Apply Gaussian Blur:</b> Reduces noise and smoothes the grayscale image.</li>
  <li><b>Canny Edge Detection:</b> Identifies potential edges in the image using gradient-based edge detection.</li>
  <li><b>Region of Interest (ROI) Masking:</b> Masks out a region of interest (typically the road ahead) to focus on lane detection within this area.</li>
  <li><b>Hough Transform:</b> Detects lines in the masked edge-detected image using the Hough transform technique.</li>
  <li><b>Line Fitting:</b> Fits lines to the detected Hough lines using linear regression or polynomial fitting.</li>
  <li><b>Visualization:</b> Draws detected lane lines onto the original image for visualization.</li>
</ul>

## Functionality
### Dependencies
<ul>
  <li><b>OpenCV (cv2):</b> Used for image processing tasks such as reading images, applying filters, and drawing lines.</li>
  <li><b>NumPy:</b> Essential for numerical operations and array manipulations.</li>
  <li><b>Matplotlib:</b> Optional, for visualizing images and plots (not used in the provided code snippet).</li>
</ul>

## How It Works
### The project's main functionalities include:

<ul>
  <li><b>Canny Edge Detection:</b> Converts the grayscale image into an edge map based on intensity gradients.</li>
  <li><b>Region of Interest Masking:</b> Focuses lane detection efforts on a specific area of the image, ignoring irrelevant regions.</li>
  <li><b>Hough Transform:</b> Identifies lines within the masked edge-detected image, essential for finding straight lines.</li>
  <li><b>Line Fitting:</b> Fits detected lines to actual lane lines, enabling accurate lane marking extraction.</li>
  <li><b>Visualization:</b> Integrates lane markings back into the original image for real-world application.</li>
</ul>
Example Usage
<ol>
  <li><b>Input:</b> Provide an image or a video frame containing road scenes with visible lane markings.</li>
  <li><b>Output:</b> Receive a processed image or video frame with annotated lane lines, aiding in autonomous driving systems or lane departure warning systems.</li>
</ol>
Implementation
The provided code snippet demonstrates lane detection using a combination of OpenCV functions for edge detection, masking, and line fitting. Adjust parameters like thresholds, region of interest, and line fitting methods based on specific road conditions and camera setups.

### Future Enhancements
<ul>
  <li>Implement advanced algorithms for lane curvature detection.</li>
  <li>Optimize performance for real-time video processing.</li>
  <li>Integrate with camera feed from autonomous vehicles or traffic monitoring systems.</li>
</ul>

### Running the Code
To run the lane detection algorithm:

<b>Clone the Repository:</b> Clone the repository containing the lane detection code.<br><br>

```bash
    git clone <repository-url>
    cd <repository-directory>
```
<b>Install Dependencies:</b> Ensure Python and necessary libraries are installed.<br><br>
    
```bash
pip install opencv-python numpy matplotlib
```
  
  
<b>Execute the Code:</b> Run the Python script to process images or video frames and visualize lane detection results.</li>

```bash
    python lane_detection.py
```

</ol>
