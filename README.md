# FitGuardian: AI Virtual Exercise Trainer  

Welcome to **FitGuardian**, a cutting-edge virtual exercise trainer capable of providing real-time feedback on your posture and movements. Using advanced technologies, including Python, OpenCV, MediaPipe, and NumPy, FitGuardian aims to enhance your workout experience by ensuring correct exercise techniques and tracking your progress dynamically.  

## Table of Contents  
- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Usage](#usage)  
- [How It Works](#how-it-works)  
- [Future Enhancements](#future-enhancements)   

## Features  
- **Real-time Pose Detection**: Utilizes MediaPipe's Pose module to detect and track body positions in real-time.  
- **Movement Analysis**: Monitors key body points, calculating angles to provide feedback on exercise form and posture.  
- **Dynamic Feedback**: Instantly alerts users about posture correctness to prevent injuries and ensure effective workouts.  
- **Progress Tracking**: Records exercise counts and calculates percentage completion, helping users stay motivated.  
- **Smooth Video Processing**: Employs OpenCV and MediaPipe for efficient video capture and processing.  
- **Interactive User Interface**: Engaging UI with visual indicators for progress and feedback to enhance the user experience.  

## Technologies Used  
- **Python**: The primary programming language driving the application's backend functionalities.  
- **OpenCV**: Used for real-time video capture and rendering; essential for displaying the webcam feed.  
- **MediaPipe**: Facilitates pose estimation, enabling the tracking of body movements and key landmarks.  
- **NumPy**: Employed for performing mathematical calculations, especially for angle assessments during exercises.  

## Installation  
Follow these steps to set up FitGuardian on your machine:  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/your-username/virtual-exercise-trainer.git
2.**Navigate to the Project Folder**:
3.**Install the Required Dependencies:**
pip install -r requirements.txt

## Usage  
To launch the FitGuardian exercise trainer, execute the following command in your terminal:

python exercise_trainer.py  
A window will pop up displaying your webcam feed. Position yourself in front of the camera and follow the on-screen instructions to begin your workout. The system will analyze your movements, providing real-time feedback regarding your posture, counting repetitions, and displaying your completion percentage. 

## How It Works
Pose Estimation: FitGuardian leverages MediaPipe's Pose module to identify 33 key landmarks on your body in real-time.
Angle Calculation: It utilizes NumPy to calculate the angles between critical points, such as the elbow, shoulder, and hip, assessing your posture and movement accuracy.
Feedback Loop: The application continuously monitors the pose data, delivering actionable feedback. For instance, if your back is not straight during a squat, the system will provide an alert immediately.

## Future Enhancements
Expanding the variety of exercises and their variations.
Improving feedback accuracy through machine learning algorithms.
Integrating voice feedback for hands-free guidance.

## Contact 
email: priiyal04@gmail.com
  
