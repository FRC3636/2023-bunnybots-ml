import time
import cv2

writer = cv2.VideoWriter('output1.avi', cv2.VideoWriter_fourcc(*'DIVX'), 3, (1280,960))
cap = cv2.VideoCapture("tcp://10.36.36.61:8000")

start_time = time.time()

if not cap.isOpened():
    print("Camera failed to open")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Could not get frame")
        break
    frame = cv2.resize(frame, (1280,960))
    writer.write(frame)
    if (time.time() - start_time) > 30:
        print("30 seconds. time is up.")
        break


cap.release()
writer.release()
cv2.destroyAllWindows()
