import cv2 as cv

def rescale_frame(frame, scale=0.75):
  
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
 
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


image = cv.imread('Images/cat_large.jpg')


rescaled_image = rescale_frame(image, scale=0.5)  


cv.imshow('Original Image', image)
cv.imshow('Rescaled Image', rescaled_image)

cv.waitKey(0)
cv.destroyAllWindows()
