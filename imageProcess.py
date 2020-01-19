import cv2
import os

while(True):
    folder = os.listdir("dataset-resized");
    for a in folder:
        if(a != ".DS_Store"):
            mylist = os.listdir("dataset-resized/" + a);
            for b in mylist:
                img = cv2.imread("dataset-resized/" + a + "/" + b);
                grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
                grayImg = cv2.resize(grayImg, (150, 150));
                cv2.imshow("image", grayImg);
        