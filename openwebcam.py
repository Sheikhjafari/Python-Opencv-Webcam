import cv2

# Open the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(1)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Display the frame
    cv2.imshow("Webcam Feed", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
