from __future__ import absolute_import, division, print_function, unicode_literals
import cv2
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import layers
import random
import pickle

camera = cv2.VideoCapture(0);

cv2.namedWindow("Image");

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 150);
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 150);

class_names = ['cardboard','glass','metal','paper','plastic','trash']

model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation = "relu", input_shape = (150,150,3)),
    keras.layers.Conv2D(32, (3, 3), activation = "relu"),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(32, (3, 3), activation = "relu"),
    keras.layers.Conv2D(32, (3, 3), activation = "relu"),
    keras.layers.MaxPooling2D(),
    keras.layers.Flatten(),
    keras.layers.Dense(256, activation = "relu"),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(6, activation = "softmax")
])
model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])
model.load_weights('./modelWeights')

while True:
    ret, frame = camera.read();
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);
    frame = cv2.resize(frame, (150, 150));
    #cv2.imshow("image", frame);
    camera_images = []
    camera_images.append(frame)
        
    camera_images = np.array(camera_images,np.uint8);
    camera_images = camera_images/255.0
    
    prediction = model.predict(camera_images)
    
    #print(class_names[np.argmax(prediction[0])])
    plt.grid(False)
    plt.imshow(camera_images[0], cmap = plt.cm.binary)
    plt.title("prediction: " + class_names[np.argmax(prediction[0])])
    plt.show()	
    
camera.release();
cv2.destroyAllWindows();
