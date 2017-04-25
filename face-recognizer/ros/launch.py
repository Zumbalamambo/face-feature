#!/usr/bin/python

import cv2, os
import sys
import numpy as np
import json
import rospy
from bridge import Bridge

cascadePath = "./cascades/haarcascade_frontalface_alt2.xml"
FACE_CASCADE = cv2.CascadeClassifier(cascadePath)

recognizer = cv2.createLBPHFaceRecognizer()

id = 0

images,labels = [],[]

def show(image):
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)         
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
        elif key == 115: #s
            global id
            id = id + 1
        elif key == 97: #a
            global id
            id = id - 1
            if id < 0:
                id = 0        
            
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        sys.exit(-1)

def run():
    bg = Bridge(show, "/usb_cam/image_raw", resize=0.75)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Exiting..."
        cv2.destroyAllWindows()

run()