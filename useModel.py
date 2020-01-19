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

modelFile = open('model.pkl','rb')
model = pickle.load(modelFile)
prediction = model.predict(test_images)
for i in range(24):
        plt.grid(False)
        plt.imshow(test_images[i], cmap = plt.cm.binary)
        plt.xlabel("Actual:" + class_names[test_labels[i]])
        plt.title("prediction: " + class_names[np.argmax(prediction[i])])
        plt.show()
