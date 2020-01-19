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

while True:
	ret, frame = camera.read();
	#gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
	cv2.imshow("Image", frame);
	cv2.waitKey(0);
	
	modelFile = open('model.pkl','rb')
	model = pickle.load(modelFile)
	prediction = model.predict(frame)
	for i in range(24):
		plt.grid(False)
		plt.imshow(frame[i], cmap = plt.cm.binary)
		plt.xlabel("Actual:" + class_names[test_labels[i]])
		plt.title("prediction: " + class_names[np.argmax(prediction[i])])
		plt.show()	
	
camera.release();
cv2.destroyAllWindows();
