import cv2

# Load the image
image = cv2.imread("image.jpeg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and black and white images
cv2.imshow("Original Image", image)
cv2.imshow("Black and White Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
