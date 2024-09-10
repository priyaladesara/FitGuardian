import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
prev_angle = 0

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)

    if len(lmList) != 0:
        # Detect shoulder press movement based on the angle between shoulder, elbow, and wrist
        shoulder = lmList[12]  # Right shoulder
        elbow = lmList[14]     # Right elbow
        wrist = lmList[16]     # Right wrist

        # Calculate the angle between shoulder, elbow, and wrist
        angle = detector.findAngle(img, 12, 14, 16)

        # Check if the angle pattern matches the shoulder press movement
        if 300 <= angle <= 320:
            if dir == 0:
                count += 1
                dir = 1
        elif 170 <= angle <= 200:
            if dir == 1:
                dir = 0

        # Display press count
        cv2.putText(img, f'Press Count: {int(count)}', (45, 670), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
