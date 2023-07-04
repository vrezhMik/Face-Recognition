import cv2
import numpy as np

# Load the Spider-Man image and resize it
spiderman_image = cv2.imread('sp.png')
spiderman_image = cv2.resize(
    spiderman_image, (0, 0), fx=0.5, fy=0.5)  # Resize by 50%
spiderman_gray = cv2.cvtColor(spiderman_image, cv2.COLOR_BGR2GRAY)

# Load the image where Spider-Man is hidden
hidden_image = cv2.imread('bg.jpeg')
hidden_gray = cv2.cvtColor(hidden_image, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(hidden_gray, spiderman_gray, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Determine the coordinates of the bounding box
top_left = max_loc
spiderman_width, spiderman_height = spiderman_image.shape[1], spiderman_image.shape[0]
bottom_right = (top_left[0] + spiderman_width, top_left[1] + spiderman_height)

# Draw the bounding box on the hidden image
cv2.rectangle(hidden_image, top_left, bottom_right, (0, 255, 0), 2)

# Display the result
cv2.imshow('Hidden Image', hidden_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
