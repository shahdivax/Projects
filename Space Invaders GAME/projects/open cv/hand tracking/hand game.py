import cv2 as c
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime= 0
cTime  = 0 

cap = c.VideoCapture(0)
detector = htm.HandDetector()

while True:
    success,img = cap.read()
    detector.findHands(img)
    lmlist = detector.findposition(img)
    if len(lmlist) != 0: #//not working check it
        print(lmlist[4]) 

    cTime = time.time()
    fps = 1/(cTime-pTime)        
    pTime = cTime

    c.putText(img,'fps : '+str(int(fps)),(30,80),c.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)

    c.imshow('img', img)
    if c.waitKey(1) & 0xFF == ord('q'):
        break