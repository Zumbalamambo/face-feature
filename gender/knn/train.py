
import sys
import numpy as np
import cv2
import os

SAMPLES = np.empty((0, 100))
RESPONSES = []
FACE_CASCADE = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_alt2.xml')

def original_train(image_file,value):
    image = cv2.imread(image_file)
    image = cv2.resize(image, (0,0), fx=0.5, fy=0.5) 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)   
        roi = gray[y:y+h, x:x+w]            
    if not len(faces) == 1:
        return         
    
    roi_small = cv2.resize(roi, (10, 10))
    sample = roi_small.reshape((1, 100))
    global SAMPLES
    SAMPLES = np.append(SAMPLES, sample, 0)        
    RESPONSES.append(value)

def edited_train(image_file,value):
    image = cv2.imread(image_file)
    image = cv2.resize(image, (0,0), fx=0.5, fy=0.5) 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    rows, cols = gray.shape
    for i in range(rows):
        for j in range(cols):
            k = gray[i,j]
            gray[i,j] = k * 0.75

    faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)   
        roi = gray[y:y+h, x:x+w]            
    if not len(faces) == 1:
        return         
    
    roi_small = cv2.resize(roi, (10, 10))
    sample = roi_small.reshape((1, 100))
    global SAMPLES
    SAMPLES = np.append(SAMPLES, sample, 0)        
    RESPONSES.append(value)

try:
    print "training males"
    for root, dirs, files in os.walk("./imdb-datasets/images/males"):
        path = root.split(os.sep)    
        for file in files:            
            original_train("./imdb-datasets/images/males/" + file,0)
            edited_train("./imdb-datasets/images/males/" + file,0)

    print "training females"
    for root, dirs, files in os.walk("./imdb-datasets/images/females"):
        path = root.split(os.sep)    
        for file in files:
            original_train("./imdb-datasets/images/females/" + file,1)
            edited_train("./imdb-datasets/images/females/" + file,1)

    print "training complete"
    np.savetxt('general-samples.data', SAMPLES)
    RESPONSES = np.array(RESPONSES, np.float32)
    RESPONSES = RESPONSES.reshape((RESPONSES.size, 1))
    np.savetxt('general-responses.data', RESPONSES)  

except KeyboardInterrupt:
    sys.exit(0)
