import cv2 , time
video = cv2.VideoCapture(0)

check, frame = video.read()

print(frame)

gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
cv2.imshow("Capturing" , frame)

#cv2.waitKey(1)


video.release()
