import cv2

# Open the webcam
cap = cv2.VideoCapture(1)

# Set the desired frame width and height
new_width = 640
new_height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, new_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, new_height)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            print("Error: Failed to grab frame.")
            break


        # Your image processing or display code goes here
        cv2.imshow('Frame', frame)

         # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()