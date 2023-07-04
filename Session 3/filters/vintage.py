import cv2
import numpy as np

# Load the image
image = cv2.imread("image.jpeg")

# Split color channels
b, g, r = cv2.split(image)

# Apply adjustments to color channels
# Increase red channel intensity
r = cv2.addWeighted(r, 1.2, np.zeros_like(r), 0, 0)
# Decrease blue channel intensity
b = cv2.addWeighted(b, 0.8, np.zeros_like(b), 0, 0)

# Merge color channels back together
filtered_image = cv2.merge((b, g, r))

# Apply vintage overlay
overlay = cv2.imread("vintage-overlay.jpeg")  # Load vintage overlay image
# Resize overlay to match image size
overlay = cv2.resize(overlay, (image.shape[1], image.shape[0]))
filtered_image = cv2.addWeighted(
    filtered_image, 0.8, overlay, 0.2, 0)  # Apply overlay

# Display the original and filtered images
cv2.imshow("Original Image", image)
cv2.imshow("Vintage Filtered Image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
