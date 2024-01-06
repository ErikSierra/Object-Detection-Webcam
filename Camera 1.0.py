import cv2
import datetime
import time

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Variables for recording logic
recording = False
last_detection_time = time.time()
detection_timeout = 5  # seconds
frame_size = (int(cap.get(3)), int(cap.get(4)))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces and bodies
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Additional checks for filtering false positives
    faces = [face for face in faces if face[2] > 30 and face[3] > 30]  # Filter out small detections
    bodies = [body for body in bodies if body[2] > 30 and body[3] > 80]  # Filter out small and non-elongated detections

    # Draw detection boxes
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Check for detections
    if len(faces) > 0 or len(bodies) > 0:
        last_detection_time = time.time()
        if not recording:
            # Start recording
            recording = True
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S%p")
            out = cv2.VideoWriter('C:/Pictures/Security Camera/' + f'{current_time}.avi', fourcc, 20.0, frame_size)
            print("Recording started")

    if recording:
        # Record current frame
        out.write(frame)

    # Stop recording if timeout reached
    if recording and (time.time() - last_detection_time > detection_timeout):
        recording = False
        out.release()
        print("Recording stopped")

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Break loop with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
if recording:
    out.release()
cap.release()
cv2.destroyAllWindows()
