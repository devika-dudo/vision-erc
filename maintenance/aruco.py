import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define the dictionary and marker parameters
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
marker_id = 42
marker_size = 200  # Marker size in pixels

# Generate the marker image
marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

# Define the size of the quiet zone (border)
quiet_zone_size = marker_size // 7  # Typically, one module width

# Add the white border around the marker
bordered_image = cv2.copyMakeBorder(
    marker_image,
    quiet_zone_size,
    quiet_zone_size,
    quiet_zone_size,
    quiet_zone_size,
    cv2.BORDER_CONSTANT,
    value=255  # White color
)

# Save the marker image with the border
cv2.imwrite('marker_42_with_border.png', bordered_image)

# Display the marker with the border
plt.imshow(bordered_image, cmap='gray', interpolation='nearest')
plt.axis('off')  # Hide axes
plt.title(f'ArUco Marker {marker_id} with Quiet Zone')
plt.show()
