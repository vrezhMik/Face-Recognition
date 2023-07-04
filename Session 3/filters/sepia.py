import cv2
import numpy as np

# Load the image
image = cv2.imread("image.jpeg")

# Apply Sepia filter
sepia_filter = np.array([[0.272, 0.534, 0.131],
                         [0.349, 0.686, 0.168],
                         [0.393, 0.769, 0.189]])
sepia_image = cv2.transform(image, sepia_filter)

# Display the original and filtered images
cv2.imshow("Original Image", image)
cv2.imshow("Sepia Filtered Image", sepia_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
