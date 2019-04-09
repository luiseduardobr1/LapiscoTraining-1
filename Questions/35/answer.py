import cv2
import numpy as np

# Read a rgb image
image = cv2.imread('image.jpg')

# Transform to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the threshold
ret, threshold_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Apply dilation
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(threshold_image, kernel, iterations=5)

# Show the input image
cv2.imshow('Input grayscale image', grayscale_image)

# Show the result of the threshold
cv2.imshow('Threshold image', threshold_image)

# Show the result of the dilation
cv2.imshow('Dilated image', dilation)
cv2.waitKey(0)
