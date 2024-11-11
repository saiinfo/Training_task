#Importing the OpenCV library
import cv2 as cv

# Read in an image
img = cv.imread('Images/cat.jpg')
cv.imshow('Normal', img)

# Converting to grayscale
# cv.cvtColor() converts the color space of the image. Here, it's converting from BGR (Blue, Green, Red) to grayscale.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray) #Displays the grayscale version of the image in a window named 'Gray'
 

# Blur 
#cv.GaussianBlur() applies a Gaussian blur (a type of image smoothing technique) to the image.
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
#cv.Canny() is an edge detection algorithm that finds the edges of objects in the image by detecting sharp intensity changes.
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)#Displaying the Canny edges

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
#cv.erode() is the opposite of dilation; it shrinks the white regions, effectively reversing the dilation process.                    The kernel size (7, 7) determines how large the erosion effect is.
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
#cv.resize() resizes the image to the specified dimensions (500, 500) in pixels.
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
#This is a slicing operation that extracts a portion of the original image.The image is sliced from row index 50 to 200 and column index 200 to 400, resulting in a cropped sub-image.
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)