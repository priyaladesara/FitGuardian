import mediapipe as mp
import cv2
import time

mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils

pose = mpPose.Pose()

cap = cv2.VideoCapture('PoseVideos/3.mp4')
pTime = 0
while True:
    success, img = cap.read()
    if not success:
        break  # If there are no more frames, exit the loop
    
    # Resize the image to a smaller size
    img = cv2.resize(img, (500, 800))  # Adjust the dimensions as needed
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
            
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime   

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for 'q' key to be pressed
        break  # If 'q' is pressed, exit the loop

cv2.destroyAllWindows()  # Close all OpenCV windows
