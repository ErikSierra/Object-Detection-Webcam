from ultralytics import YOLO
import cv2
import random
import math 
# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO(r"C:\Coding Stuff\Python Projects\Security_Camera\models\yolov8x.pt")

# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]
# Create a dictionary mapping class names to colors (RGB)
class_colors = {className: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for className in classNames}

min_confidence_threshold = 0.9

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # Coordinates and drawing box outlines
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # Confidence as an integer percentage
            confidence = int(box.conf[0] * 100)

            # Check if the detection meets the minimum confidence threshold
            if confidence >= min_confidence_threshold:
                # Bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # Class name with confidence
                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f"{class_name} {confidence}%"

                # Get the color for this class
                color = class_colors[class_name]

                # Draw bounding box and text with the class-specific color
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                org = (x1, y1 - 10)
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 0.5
                thickness = 1
                cv2.putText(img, label, org, font, fontScale, color, thickness)


    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()