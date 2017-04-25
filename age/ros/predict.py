#! /usr/bin/env python

import cv2
import time
from bridge import Bridge
import rospy
import numpy as np

samples = np.loadtxt('./trained-data/age-samples.data', np.float32)
responses = np.loadtxt('./trained-data/age-responses.data', np.float32)
responses = responses.reshape((responses.size,1))

FACE_CASCADE = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_alt2.xml')

model = cv2.KNearest()
model.train(samples,responses)

def show(image):
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)        
    try:         
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
        face_loc = {'x':0,'y':0}
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)   
            roi = gray[y:y+h, x:x+w]
            face_loc['x'] = x
            face_loc['y'] = y        

            roi_small = cv2.resize(roi,(10,10))
            roi_small = roi_small.reshape((1,100))
            roi_small = np.float32(roi_small)

            retval, results, neigh_resp, dists = model.find_nearest(roi_small
                        , k = 1)
            
            age = int(results[0][0])
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image,str(age),(face_loc['x'],face_loc['y']), font, 0.5, (200,255,155), 2)
        cv2.imshow('webcam', image)
        cv2.waitKey(1)            
    except KeyboardInterrupt:
        raise        


def run():
    bg = Bridge(show, "/usb_cam/image_raw", resize=0.75)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Exiting..."
        cv2.destroyAllWindows()

run()