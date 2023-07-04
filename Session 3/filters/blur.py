import cv2

# Load the image
image = cv2.imread("image.jpeg")

# Apply Gaussian blur
ksize = (5, 5)  # Kernel size, larger values result in stronger blur
sigmaX = 0  # Standard deviation in the X direction (horizontal)
blurred_image = cv2.GaussianBlur(image, ksize, sigmaX)

# Display the original and blurred images
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
