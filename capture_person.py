import cv2
import os

# Specify the directory to save the images
output_dir = 'captured_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Capture and save 500 frames
num_images = 500
count = 0

while count < num_images:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Error: Could not read frame.")
        break

    # Construct the filename and save the frame
    filename = os.path.join(output_dir, f'image_{count:04d}.png')
    cv2.imwrite(filename, frame)

    print(f'Captured {filename}')
    count += 1

    # Display the frame (optional)
    cv2.imshow('Frame', frame)

    # Press 'q' to quit early (optional)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
