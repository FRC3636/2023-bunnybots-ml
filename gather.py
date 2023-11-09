import time
import cv2

cap = cv2.VideoCapture('tcp://10.36.36.61:8000')
writer = cv2.VideoWriter('output1.avi', cv2.VideoWriter_fourcc(*'MJPG'), cap.get(cv2.CAP_PROP_FPS), (1280,960))

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
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
writer.release()
cv2.destroyAllWindows()
