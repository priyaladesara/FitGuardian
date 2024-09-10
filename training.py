import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models

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

# Load the dataset
dataset_dir = 'your/dataset/directory'
images, labels = load_dataset(dataset_dir)

# Split the dataset into training and testing sets
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

# Normalize pixel values
train_images = train_images / 255.0
test_images = test_images / 255.0

# Define the model architecture
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dense(3, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# Save the model
model.save('exercise_classifier_model')
