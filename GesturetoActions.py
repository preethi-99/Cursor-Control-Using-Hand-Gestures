import cv2
import numpy as np
import HandDetectionTracking as htm
import time
import autopy

wCam, hCam = 960, 720
frameR = 100
smoothening = 7

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()

while True:
    # Detect Hand
    success, img = cap.read()
    print(success)
    print(img)
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
    
    # Detect Fingers
    fingers = detector.fingersUp()

    # Fingers used in gestures
    print("Fingers 1") # Index Finger
    print(fingers[1])
    print("Fingers 2") # Middle Finger
    print(fingers[2])
    print("Fingers 0") # Thumb
    print(fingers[0])
    
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
    (255, 0, 255), 2)

    #Only Index finger cursor movement
    if fingers[1] == 1 and fingers[2] == 0 and fingers[0] == 0:
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening
    
        # Mouse Hover
        autopy.mouse.move(wScr - clocX, clocY)
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY
        
    #Index, middle finger, no Thumb. Left Click
    if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 0:
        autopy.mouse.click()
        a
    # Thumb only. Right Click
    if fingers[1] == 0 and fingers[2] == 0 and fingers[0] == 1:
        autopy.mouse.click(autopy.mouse.Button.RIGHT)


    
    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
    (255, 0, 0), 3)
    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)