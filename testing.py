import os
import numpy as np
import cv2
from sklearn.metrics import accuracy_score
import tensorflow as tf

# Function to load images and labels from the dataset directory
def load_dataset(dataset_dir):
    images = []
    labels = []
    exercise_mapping = {'curl': 0, 'press': 1, 'squats': 2}

    for exercise in exercise_mapping.keys():
        exercise_dir = os.path.join(dataset_dir, exercise)
        for filename in os.listdir(exercise_dir):
            if filename.endswith('.jpg'):
                image = cv2.imread(os.path.join(exercise_dir, filename))
                image = cv2.resize(image, (224, 224))
                images.append(image)
                labels.append(exercise_mapping[exercise])

    return np.array(images), np.array(labels)

# Load the test dataset
dataset_dir = 'your/test/dataset/directory'
test_images, test_labels = load_dataset(dataset_dir)

# Normalize pixel values
test_images = test_images / 255.0

# Load the trained model
model = tf.keras.models.load_model('exercise_classifier_model')

# Make predictions on the test set
predictions = model.predict(test_images)
predicted_labels = np.argmax(predictions, axis=1)

# Calculate accuracy
accuracy = accuracy_score(test_labels, predicted_labels)
print("Test Accuracy:", accuracy)
