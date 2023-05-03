import cv2

video = cv2.VideoCapture('E:\cars\Teslas Avoiding Accidents Compilation.mp4')
classifier_file = "Car_Tracker.xml"
car_detector = cv2.CascadeClassifier('E:\cars\cars.xml')
pedestrians_detector = cv2.CascadeClassifier('E:\cars\pedestrians.xml')
print('hello')
while True:
    (read_successful, frame) = video.read()
    if read_successful:
        # process the frame
        black_n_white = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    car_coordinates = car_detector.detectMultiScale(black_n_white)
    pedestrians_coordinate = pedestrians_detector.detectMultiScale(black_n_white)
    for (x, y, w, h) in car_coordinates:
        cv2.rectangle(frame, (x,y), (x+y, y+h), (0,255,0), 2)
    for (x, y, w, h) in pedestrians_coordinate:
        cv2.rectangle(frame, (x,y), (x+y, y+h), (0,255,255), 2)
    cv2.imshow("Sample", frame)
    key = cv2.waitKey(1)

    if key == 81:
        break
video.release()