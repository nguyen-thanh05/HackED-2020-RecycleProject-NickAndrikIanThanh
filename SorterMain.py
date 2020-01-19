from __future__ import absolute_import, division, print_function, unicode_literals
import cv2
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import layers
import random
import serial

devices = os.listdir("/dev")
for device in devices:
    if device[0:6] == "ttyUSB":
        ser = serial.Serial("/dev/"+device, 9600)
        break

for device in devices:
    if device[0:5] == "video":
        try:
            camera = cv2.VideoCapture(int(device[5:]));
            ret, frame = camera.read();
            cv2.imshow('Camera Stream',frame)
            c = cv2.waitKey(0)
            # video stream is correct stream
            if (c == 13):
                print("test")
                videoDevice = int(device[5:])
                camera.release()
                cv2.destroyAllWindows();
                break
            # video stream is not correct
            if (c == 32):
                continue
        # video stream invalid
        except:
            continue

else:
    print("Error")
#ser = serial.Serial('/dev/ttyUSB', 9600)
def send_class(classification):
    if (classification == "garbage"):
        ser.write(b'g')
    elif (classification == "recycle"):
        ser.write(b'r')
    elif (classification == "compost"):
        ser.write(b'c')

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

class_names = ['cardboard','glass','metal','paper','plastic','trash']
bins = ['recycle','recycle','recycle','compost','garbage','garbage']
while True:
    camera = cv2.VideoCapture(videoDevice);
    #ret, frame = camera.read();
    #cv2.imshow('Input',frame)
    #c = cv2.waitKey(0)
    while (True):
        ret, frame = camera.read();
        cv2.imshow('Input',frame)
        c = cv2.waitKey(1)
        if (c!= -1):
            break

    if (c == 27):
        break


    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);
    frame = cv2.resize(frame, (150, 150));
    camera_images = []
    camera_images.append(frame)
    camera_images = np.array(camera_images,np.uint8);
    camera_images = camera_images/255.0

    prediction = model.predict(camera_images)
    print(bins[np.argmax(prediction[0])] + " - " + class_names[np.argmax(prediction[0])])
    send_class(bins[np.argmax(prediction[0])])
    camera.release()
    cv2.destroyAllWindows();
camera.release();
cv2.destroyAllWindows();
