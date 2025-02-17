import cv2
import numpy as np

# Load the image
image = cv2.imread('marker_42_with_border.png')

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or unable to load.")
    exit()

# Define the ArUco dictionary and parameters
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

# Create the ArUco detector
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

# Detect the markers
corners, ids, rejected = detector.detectMarkers(image)  # Use the original color image here

# Print the detected markers
if ids is not None:
    print("Detected markers:", ids)
    # Draw detected markers
    cv2.aruco.drawDetectedMarkers(image, corners, ids)
    # Display the image with detected markers
    cv2.imshow('Detected Markers', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No markers detected.")
