#Object Detection Webcam
#Erik Sierra
#Last Updated: 1/07/23

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from ultralytics import YOLO
import cv2
import math
import time
import os
import datetime

# Create the directory if it doesn't exist
save_dir = "C:/Pictures/Security Camera"
os.makedirs(save_dir, exist_ok=True)

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Load the YOLOv8 model
model = YOLO(r"C:\Coding Stuff\Python Projects\Security_Camera\models\yolov8l.pt")

# Email configuration
USER = "youremail@email.com"  # Your Gmail address
PASS = "abcd abcd abcd abcd"  # Your app password


def send_email(subject, message, image_path=None):
    msg = MIMEMultipart()
    msg['From'] = USER
    msg['To'] = USER
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    if image_path:
        with open(image_path, 'rb') as f:
            mime = MIMEImage(f.read(), _subtype="jpg")
            mime.add_header('Content-Disposition', 'attachment', filename=os.path.basename(image_path))
            msg.attach(mime)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(USER, PASS)
        server.sendmail(USER, USER, msg.as_string())
        print("Email sent successfully")


# Main object detection and email sending logic
record = False
person_detected_time = None
email_delay = 600  # Delay in seconds (10 minutes)
last_email_time = None
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None

while True:
    success, img = cap.read()
    results = model(img, stream=True)
    person_detected_in_this_frame = False

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            class_name = model.names[cls]

            if class_name == 'person':
                person_detected_in_this_frame = True
                current_time = time.time()

                if person_detected_time is None:
                    person_detected_time = current_time

                elapsed_time = current_time - person_detected_time
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = int(box.conf[0] * 100)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 1)
                label = f"{class_name} {confidence}%"
                cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)

                if elapsed_time > 1.5 and (last_email_time is None or (current_time - last_email_time) >= email_delay):
                    # Save the current frame as an image
                    detected_image_path = f"{save_dir}/detected_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                    cv2.imwrite(detected_image_path, img)

                    # Send email with the captured image
                    last_email_time = current_time
                    send_email("Person Detected", "A person has been detected in the frame", detected_image_path)

                if not record:
                    record = True

    if not person_detected_in_this_frame:
        person_detected_time = None

    if record and (time.time() - person_detected_time <= 1.5):
        if out is None:
            current_time = datetime.datetime.now().strftime("%m_%d_%Y_%I%M%p")
            out = cv2.VideoWriter(f'{save_dir}/{current_time}.avi', fourcc, 20.0, (640, 480))
        out.write(img)
    else:
        record = False
        if out:
            out.release()
            out = None

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
if out:
    out.release()
cv2.destroyAllWindows()
