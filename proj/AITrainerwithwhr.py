import cv2
import numpy as np
import time
import math
import PoseModule as pm

cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
curl_flag = False  # Flag to indicate if curls are being performed
visibility_threshold = 0.5  # Adjust visibility threshold as needed

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)

    if len(lmList) != 0:
        # Extract landmarks for relevant joints
        shoulder = lmList[11]  # Shoulder landmark
        elbow = lmList[13]  # Elbow landmark
        wrist = lmList[15]  # Wrist landmark

        # Calculate angle to check hand position
        angle = detector.findAngle(img, 12, 14, 16)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))

        # Check if hand is straight in front of the screen, not behind the body, or slightly tilted
        correct_hand_position = shoulder[2] < elbow[2] < wrist[2] and wrist[1] < shoulder[1] + 80  # Adjust threshold as needed

        # Update curls count if hand position is correct and curl_flag is True
        if per == 100:
            if correct_hand_position and curl_flag:
                if dir == 0:
                    count += 0.5
                    dir = 1
            else:
                dir = 0  # Reset the counting direction

        # Draw Bar
        color = (255, 0, 255)
        if correct_hand_position:
            color = (0, 255, 0)
            curl_flag = True  # Set curl_flag to True if hand position is correct
        else:
            curl_flag = False  # Reset curl_flag to False if hand position is incorrect
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)

        # Draw Curl Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 25)

        # Add text for correcting posture if hand position is incorrect and hand is not fully visible
        if not correct_hand_position and not curl_flag and wrist[2] < visibility_threshold:
            cv2.putText(img, "Please correct hand position", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
