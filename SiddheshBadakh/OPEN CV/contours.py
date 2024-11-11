import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('Images/cat.jpg')
cv.imshow('Cats', img)

# Create a blank image (same size as the original)
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Apply Gaussian blur to the grayscale image
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Use Canny edge detection
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Optionally apply thresholding (commented out)
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

# Find contours based on Canny edges
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# Draw the contours on the blank image
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
