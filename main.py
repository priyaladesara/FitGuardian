import mediapipe as mp
import cv2
import numpy as np
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('exercise_classifier_model')

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Open the camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe Pose
    results = pose.process(rgb_frame)

    # If pose landmarks are detected
    if results.pose_landmarks:
        # Get landmarks
        landmarks = np.array([[landmark.x, landmark.y] for landmark in results.pose_landmarks.landmark]).flatten()

        # Preprocess the image for the model
        processed_image = np.expand_dims(cv2.resize(frame, (224, 224)), axis=0) / 255.0

        # Predict exercise
        prediction = model.predict(processed_image)

        # Get the exercise label
        exercise = ["curl", "press", "squats"][np.argmax(prediction)]

        # Display the exercise label
        cv2.putText(frame, exercise, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Virtual Personal Trainer', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
