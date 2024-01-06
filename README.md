# Object-Detection-Webcam
This is a desktop webcam utilizing the YOLOv8 (You Only Look Once) model to detect persons in a closed environment.

Process:
1. Observe the environment, while detecting objects included in the pre-trained library
2. Labels detected objects with outline, name, and confidence level
3. When a person is detected, automatic recording initiates until the person is no longer detected for five seconds or more. When recording stops, the video is saved to local C: drive
4. When a person is detected, an automatic email notification is sent to the selected receipient with a description and screenshot of the detected person at a single time



