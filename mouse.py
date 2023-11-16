import time
import cv2
import numpy as np
import HandTrackingModule as htm
import pyautogui

cap = cv2.VideoCapture(0)
#turn my camera on


cTime = 0
pTime = 0
detector = htm.handDetector(maxHands=1, detectionCon=True)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    

    cTime = time.time() 
    
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
