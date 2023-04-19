#Submitted By Lakshay Jain
#102103642
#2co23

import cv2

cars_cascade = cv2.CascadeClassifier('cars.xml')

def detect_cars(frame):
    cars = cars_cascade.detectMultiScale(frame, 1.15, 4)
    if len(cars) > 0:
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
        return True
    else:
        return False

def main():

    CarVideo = cv2.VideoCapture('Sample4.mp4')
    while CarVideo.isOpened():
        ret, frame = CarVideo.read()
        org = (30, 50)
        controlkey = cv2.waitKey(1)
        if ret:
            cars_detected = detect_cars(frame)
            if cars_detected:
                cv2.putText(frame, 'Vehicle Detected', org, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                # print("Vehicle Behind")
            else:
                # print("Path Clear")
                cv2.putText(frame, 'Path Clear', org, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow('frame', frame)
        else:
            break
        if controlkey == ord(' '):
            break

    CarVideo.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()