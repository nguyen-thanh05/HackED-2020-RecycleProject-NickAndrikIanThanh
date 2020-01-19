from __future__ import absolute_import, division, print_function, unicode_literals
import cv2
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import layers
import random

#TO BE CHANGED
train_images = []
train_labels = []
test_images = []
test_labels = []
class_names = ['cardboard','glass','metal','paper','plastic','trash']

folder = os.listdir("dataset-resized");
for a in folder:
    count = 0
    if(a != ".DS_Store"):
        mylist = os.listdir("dataset-resized/" + a);
        for b in mylist:
            img = cv2.imread("dataset-resized/" + a + "/" + b);
            grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
            grayImg = cv2.resize(grayImg, (250, 250));
            if (count <=3):
                test_images.append(grayImg)
                test_labels.append(class_names.index(a))
                count += 1
            else:
                train_images.append(grayImg)
                train_labels.append(class_names.index(a))

for i in range(1000):
    indexA = random.randint(0,len(train_images)-1)
    indexB = random.randint(0,len(train_images)-1)
    tempImage = train_images[indexA]
    tempLabel = train_labels[indexA]
    train_images[indexA] = train_images[indexB]
    train_labels[indexA] = train_labels[indexB]
    train_images[indexB] = tempImage
    train_labels[indexB] = tempLabel

train_images = np.array(train_images,np.uint8)
train_labels = np.array(train_labels,np.uint8)
test_images = np.array(train_images,np.uint8)
test_labels = np.array(train_labels,np.uint8)
# ~ data = keras.datasets.fashion_mnist
# ~ (train_images, train_labels), (test_images, test_labels) = data.load_data()
train_images = train_images/255.0
test_images = test_images/255.0

# ~ class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               # ~ 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


model = keras.Sequential([
    keras.layers.Flatten(input_shape = (250,250)),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(6, activation = "softmax")
    ])
model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])
model.fit(train_images, train_labels, epochs = 10)
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("tested acc: ", test_acc)
prediction = model.predict(test_images)
for i in range(24):
        plt.grid(False)
        plt.imshow(test_images[i], cmap = plt.cm.binary)
        plt.xlabel("Actual:" + class_names[test_labels[i]])
        plt.title("prediction: " + class_names[np.argmax(prediction[i])])
        plt.show()
