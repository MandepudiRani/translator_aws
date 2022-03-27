import cv2
import numpy as np
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)

fist = cv2.CascadeClassifier('fist.xml')
face = cv2.CascadeClassifier('face.xml')
palm = cv2.CascadeClassifier('palm.xml')
ret, photo = cap.read()
fist_detection = fist.detectMultiScale(photo)
    #face_detection = face.detectMultiScale(photo)
palm_detection = palm.detectMultiScale(photo)
if len(fist_detection)==0:
    print('no detection')
else:
    x1 = fist_detection[0][0]
    y1 = fist_detection[0][1]
    x2 = fist_detection[0][2] + x1
    y2 = fist_detection[0][3] + y1
    rphoto = cv2.rectangle(photo, (x1,y1), (x2,y2), color = (255,255,255))
    cv2.imshow('hi' , photo)
    cv2.putText(photo,"Why da", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(209, 80, 0, 255),3)
    print('detection fist')
if len(palm_detection)==0:
    print('no detection')
else:
    x1 = palm_detection[0][0]
    y1 = palm_detection[0][1]
    x2 = palm_detection[0][2] + x1
    y2 = palm_detection[0][3] + y1
    rphoto = cv2.rectangle(photo, (x1,y1), (x2,y2), color = (255,255,255))
    cv2.imshow('hi' , photo)
    cv2.putText(photo,"Hello da", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(209, 80, 0, 255),3)
    print('detection palm')
cv2.destroyAllWindows()
