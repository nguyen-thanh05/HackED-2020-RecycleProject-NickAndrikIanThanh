import cv2

camera = cv2.VideoCapture(0);

cv2.namedWindow("Image");

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 28);
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 28);

while True:
	ret, frame = camera.read();
	gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
	cv2.imshow("Image", gray_image);
	cv2.imwrite("Image.jpg", frame);
	if cv2.waitKey(30) & 0xFF == ord('q'):
        	break

camera.release();
cv2.destroyAllWindows();
