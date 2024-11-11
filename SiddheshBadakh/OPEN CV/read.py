#import cv2 as cv
#img=cv.imread('images/cat.jpg')
#cv.imshow('cat',img)
#cv.waitKey(0)


import cv2 as cv
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()


