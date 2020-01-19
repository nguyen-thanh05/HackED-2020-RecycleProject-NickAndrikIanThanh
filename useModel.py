from __future__ import absolute_import, division, print_function, unicode_literals
import cv2
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import layers
import random

test_images = []
test_labels = []
class_names = ['cardboard','glass','metal','paper','plastic','trash']

folder = os.listdir("dataset-resized");
for a in folder:
    count = 0
    if(a != ".DS_Store" and a != ".directory"):
        mylist = os.listdir("dataset-resized/" + a);
        for b in mylist:
            img = cv2.imread("dataset-resized/" + a + "/" + b);
            grayImg = cv2.resize(img, (150, 150));
            if (count <=3):
                test_images.append(grayImg)
                test_labels.append(class_names.index(a))
                count += 1
            else:
                break
            
test_images = np.array(test_images,np.uint8)
test_labels = np.array(test_labels,np.uint8)
test_images = test_images/255.0

model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation = "relu", input_shape = (150,150,3)),
    keras.layers.Conv2D(32, (3, 3), activation = "relu"),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(32, (3, 3), activation = "relu"),
    keras.layers.Conv2D(32, (3, 3), activation = "relu"),
    keras.layers.MaxPooling2D(),
    keras.layers.Flatten(),#input_shape = (150,150,3)),
    keras.layers.Dense(256, activation = "relu"),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(6, activation = "softmax")
    ])
model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])
model.load_weights('./modelWeights')
prediction = model.predict(test_images)
for i in range(24):
        plt.grid(False)
        plt.imshow(test_images[i], cmap = plt.cm.binary)
        plt.xlabel("Actual:" + class_names[test_labels[i]])
        plt.title("prediction: " + class_names[np.argmax(prediction[i])])
        plt.show()
