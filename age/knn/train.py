
import sys
import numpy as np
import cv2
import os

SAMPLES = np.empty((0, 100))
RESPONSES = []
FACE_CASCADE = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_alt2.xml')

FEMALE_FACTOR = 1.2
MALE_FACTOR = 0.9
GRAY_FACTOR = 0.6

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
            gray[i,j] = k * GRAY_FACTOR

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
            index = file.index('+')
            age = 2017 - int(file[index+1:index+5])   
            age = age * MALE_FACTOR

            original_train("./imdb-datasets/images/males/" + file,age)
            edited_train("./imdb-datasets/images/males/" + file,age)

    print "training females"
    for root, dirs, files in os.walk("./imdb-datasets/images/females"):
        path = root.split(os.sep)    
        for file in files:
            index = file.index('+')
            age = 2017 - int(file[index+1:index+5])
            age = age * FEMALE_FACTOR

            original_train("./imdb-datasets/images/females/" + file,age)
            edited_train("./imdb-datasets/images/females/" + file,age)

    print "training complete"
    np.savetxt('general-samples.data', SAMPLES)
    RESPONSES = np.array(RESPONSES, np.float32)
    RESPONSES = RESPONSES.reshape((RESPONSES.size, 1))
    np.savetxt('general-responses.data', RESPONSES)  

except KeyboardInterrupt:
    sys.exit(0)
