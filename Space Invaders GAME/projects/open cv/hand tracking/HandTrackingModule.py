import cv2 as c
import mediapipe as mp
import time

faceCascade= c.CascadeClassifier("C:/Users/lenovo/Desktop/Space Invaders GAME/projects/resources/haarcascade_frontalface_default.xml")

cap = c.VideoCapture(0)

class HandDetector():
    def  __init__(self,mode=False,maxHands = 2,detectionCon = 0.5,trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.derectionCon = detectionCon
        self.trackCon = trackCon
         
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.derectionCon,self.trackCon)
        self.mpDraw  = mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
        imgrgb = c.cvtColor(img,c.COLOR_BGR2RGB)
        self.results = self.hands.process(imgrgb)
        #print(results.multi_hand_lamdmarks)
        '''
        #(for face decetation together)
        gray = c.cvtColor(img,c.COLOR_BGR2GRAY)
    
        faces = faceCascade.detectMultiScale(gray,1.1,4)
        for (x,y,w,h) in faces:
            c.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        '''
        if self.results.multi_hand_landmarks:
           for HandLms in self.results.multi_hand_landmarks:
               if draw:
                    self.mpDraw.draw_landmarks(img,HandLms,self.mpHands.HAND_CONNECTIONS) 
        return img

    def findposition(self,img,handNo = 0 ,draw=True):

        lmlist=[]
        if self.results.multi_hand_landmarks: 
            myHand=self.results.multi_hand_landmarks[handNo]

            for id , lm in  enumerate(myHand.landmark):
                #print(id,lm)
                h , w , cc, = img.shape
                cx , cy = int(lm.x*w), int(lm.y*h)
                #print(id,cx,cy)
                lmlist.append([id,cx,cy])
                if draw:
                    c.circle(img,(cx,cy),5,(255,0,255),c.FILLED)  
        return lmlist

def main():
    pTime= 0
    cTime  = 0 

    cap = c.VideoCapture(0)
    detector = HandDetector()

    while True:
        success,img = cap.read()
        img = detector.findHands(img)
        
        lmlist = detector.findposition(img)
        #if len(lmlist) != 0: //not working check it
            #print(lmlist[4])

        cTime = time.time()
        fps = 1/(cTime-pTime)        
        pTime = cTime

        c.putText(img,'fps : '+str(int(fps)),(30,80),c.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)

        c.imshow('img', img)
        if c.waitKey(1) & 0xFF == ord('q'):
            break
     

 




if __name__ == '__main__':
    main()
 