import cv2 as c
import mediapipe as mp
import time

faceCascade= c.CascadeClassifier("C:/Users/lenovo/Desktop/Space Invaders GAME/projects/resources/haarcascade_frontalface_default.xml")

cap = c.VideoCapture(0)


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw  = mp.solutions.drawing_utils

pTime= 0
cTime  = 0 

while True:
    success,img = cap.read()
    imgrgb = c.cvtColor(img,c.COLOR_BGR2RGB)
    results = hands.process(imgrgb)
    #print(results.multi_hand_lamdmarks)
    '''
    #(for face decetation together)
    gray = c.cvtColor(img,c.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        c.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    '''
    if results.multi_hand_landmarks:
        for HandLms in results.multi_hand_landmarks:
            for id , lm in  enumerate(HandLms.landmark):
                #print(id,lm)
                h , w , cc, = img.shape
                cx , cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                #if id == 4:
                c.circle(img,(cx,cy),5,(255,0,255),c.FILLED)


            mpDraw.draw_landmarks(img,HandLms,mpHands.HAND_CONNECTIONS) 

    cTime = time.time()
    fps = 1/(cTime-pTime)        
    pTime = cTime

    c.putText(img,'fps : '+str(int(fps)),(30,80),c.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)

    c.imshow('img', img)
    if c.waitKey(1) & 0xFF == ord('q'):
         break
