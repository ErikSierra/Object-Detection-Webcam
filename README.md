**Desktop Webcam Object Detection with Ultralytics YOLOv8:**

This project harnesses the power of Ultralytics YOLOv8 (You Only Look Once) model to perform real-time object detection, specifically focusing on detecting persons in a closed environment using a desktop webcam.

**Process:**

1. **Observation and Detection:**
   - The system continuously observes the environment through the webcam.
   - It employs the YOLOv8 model to detect objects, including persons, based on its pre-trained library.
   - Detected objects are labeled with an outline, name, and confidence level for easy identification.

2. **Recording and Saving:**
   - Upon detecting a person, the system automatically initiates video recording.
   - Recording continues until the person is no longer detected for five seconds or more.
   - Recorded videos are saved locally on the C: drive for future reference and analysis.

3. **Email Notification:**
   - In addition to recording, the system triggers an automatic email notification when a person is detected.
   - The email includes a detailed description of the detected person, along with a screenshot captured at the time of detection.
   - This feature enables users to receive real-time alerts and take appropriate actions as needed.

***Note:*** 
The provided .py file serves as a starting point and requires customization with your own models and directories for seamless integration into your environment.

**Resources:**
- [Ultralytics Website](https://www.ultralytics.com/)
- [Ultralytics YOLOv8 GitHub](https://github.com/ultralytics/ultralytics)

**Additional Information:**

- **YOLOv8 Model Performance:** YOLOv8 is known for its exceptional performance in real-time object detection tasks, making it suitable for various applications, including surveillance, security, and automation.
  
- **Customization and Extension:** While this project focuses on person detection, the YOLOv8 model can be customized and extended to detect other objects based on specific requirements. With ample documentation and support from Ultralytics, users can tailor the model to suit their unique use cases.

- **Scalability and Deployment:** The lightweight nature of YOLOv8 allows for easy deployment on various hardware platforms, including desktops, edge devices, and even embedded systems. Its scalability makes it ideal for both small-scale projects and large-scale deployments across multiple locations.


![image](https://github.com/ErikSierra/Object-Detection-Webcam/assets/120680439/6bcaf18c-6c7e-4f74-bead-cfcd2cf6788a)!
![image](https://github.com/ErikSierra/Object-Detection-Webcam/assets/120680439/d7c1e7e7-a036-4681-9f43-767f5868ac9c)



![243418624-5785cb93-74c9-4541-9179-d5c6782d491a](https://github.com/ErikSierra/Object-Detection-Webcam/assets/120680439/e863233d-5bc7-4af1-8920-a864f543fe0d)


