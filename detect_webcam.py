from ultralytics import YOLO
import cv2

# Load the model
model = YOLO("best.pt")

# Open webcam
cap = cv2.VideoCapture(0)  # 0 for default webcam, change to 1 or 2 if you have multiple

while True:
    ret, frame = cap.read()
    
    # Perform prediction
    results = model(frame)
    
    # Iterate through each result
    for pred in results.pandas().xyxy[0].values:
        # Get coordinates and labels
        xmin, ymin, xmax, ymax = int(pred[0]), int(pred[1]), int(pred[2]), int(pred[3])
        label = pred[-1]
        
        # Draw bounding box
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Show the frame
    cv2.imshow('YOLOv5 Object Detection', frame)
    
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
