import cv2

camera = cv2.VideoCapture(0);

cv2.namedWindow("Image");

ret, frame = camera.read();

cv2.imshow("Image", frame);


