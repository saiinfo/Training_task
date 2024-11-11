import cv2

# Open video file from the specified path
cap = cv2.VideoCapture("videos/dog.mp4")  # Path to the video

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()  # Read the frame

    if not ret:
        print("Error: Could not read frame. Exiting...")
        break

    # Get width and height of the frame
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("Width ==>", width)
    print("Height==>", height)
    
    # Resize frame
    frame = cv2.resize(frame, (700, 450))

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Flip the frame
    frame = cv2.flip(frame, -1)

    # Display the original color frame and grayscale frame
    cv2.imshow('Color Frame', frame)
    cv2.imshow("Gray Frame", gray)

    # Exit if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
