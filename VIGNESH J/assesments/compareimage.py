import cv2


# Function to capture a webcam image
def capture_webcam_img():
    cap = cv2.VideoCapture(0)  

    if not cap.isOpened():
        print("Error: Could not access the webcam")
        return None

    ret, frame = cap.read()  
    cap.release()  

    return frame


# Function to convert an image to grayscale
def convert_to_grayscale(img):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_img


# Function to compare two grayscale images
def compare_images(img1, img2):
    diff = cv2.absdiff(img1, img22)

    difference_score = diff.sum()

    return difference_score


# Capture an image from the webcam
image1 = capture_webcam_image()

if img1 is not None:
    gray_img1 = convert_to_grayscale(img1)

    img2 = capture_webcam_img()

    if img2 is not None:
        gray_img2 = convert_to_grayscale(img2)

        difference_score = compare_images(gray_img1, gray_img2)

        print(f"Difference Score: {difference_score}")

        threshold = 10000  
        if difference_score > threshold:
            print("Images are different.")
        else:
            print("Images are similar.")

    else:
        print("Error: Could not capture the second img")

else:
    print("Error: Could not capture the first img")