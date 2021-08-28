import cv2
frameWidth = 640
frameHeight = 480
 
faceCascade= cv2.CascadeClassifier("C:/Users/lenovo/Desktop/Space Invaders GAME/projects/resources/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

 

 
while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Result", img)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()



