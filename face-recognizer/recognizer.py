#!/usr/bin/python

import cv2, os
import sys
import numpy as np
import json

cascadePath = "./cascades/haarcascade_frontalface_alt2.xml"
FACE_CASCADE = cv2.CascadeClassifier(cascadePath)

recognizer = cv2.createLBPHFaceRecognizer()

id = 0

images,labels = [],[]

try:
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, image = cam.read()        
        image = cv2.resize(image, (0,0), fx=0.5, fy=0.5) 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:            
            face = gray[y: y + h, x: x + w]                        
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)            
            font = cv2.FONT_HERSHEY_SIMPLEX            

            if len(labels) > 0:
                face_id, conf = recognizer.predict(face)                
                cv2.putText(image,str(id) + "->" + str(face_id),(x,y-5), font, 0.4, (200,255,155), 2)
            else:
                cv2.putText(image,str(id),(x,y-5), font, 0.4, (200,255,155), 2)                

        cv2.imshow('webcam', image)
        key = cv2.waitKey(1) & 0XFF        
        if key == 32:                        
            images.append(face)
            labels.append(id)
            recognizer.train(images, np.array(labels))            
        elif key == 27: #space
            break
        elif key == 115: #s
            id = id + 1
        elif key == 97: #a
            id = id - 1
            if id < 0:
                id = 0            
        
    cam.release()
    cv2.destroyAllWindows()
        
except KeyboardInterrupt:
    cv2.destroyAllWindows()
    sys.exit(-1)