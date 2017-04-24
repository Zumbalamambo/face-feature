
import cv2
import sys

FACE_CASCADE = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_alt2.xml')

try:
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, image = cam.read()        
        image = cv2.resize(image, (0,0), fx=0.5, fy=0.5) 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            # mouth = gray[y+int(h*0.6):y+h,x+int(w*0.25):x+int(w*0.75)]
            cv2.rectangle(image,(x+int(w*0.25),y+int(h*0.6)),(x+int(w*0.75),y+h),(255,0,0),2)

        cv2.imshow('webcam', image)
        cv2.waitKey(1)
        
except KeyboardInterrupt:
    cv2.destroyAllWindows()
    sys.exit(-1)