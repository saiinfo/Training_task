import cv2

# Open the default camera (usually the first webcam)
video = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not video.isOpened():
    print("Error: Could not open webcam")
    
# Loop to capture video stream
while True:
    ret, frame = video.read()  # Capture a frame
    if not ret:
        break

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Press 'q' to exit the webcam stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
video.release()
cv2.destroyAllWindows()
