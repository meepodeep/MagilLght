import numpy as np
import cv2
import mediapipe as mp
import time 
import threading

cxInverse = 0
cursor_cx_global = 0
cursor_cy_global = 0
thumb_cx_global = 0
thumb_cy_global = 0
pointer_cx_global = 0
pointer_cy_global = 0
middle_cx_global = 0
middle_cy_global = 0
ret = False
LightPosFreeze = False
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

   
def FindHands(cam,):
    global cursor_cx_global
    global cursor_cy_global
    global thumb_cx_global 
    global thumb_cy_global 
    global pointer_cx_global 
    global pointer_cy_global 
    global middle_cx_global
    global middle_cy_global
    while True:
        
        ret, frame = cam.read()
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (1920, 1080))
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:

            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cursor_cy_global = cy
                    cursor_cx_global = cx
                    if id == 0:
                        cv2.circle(frame, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                        
                    if id == 4:
                        thumb_cx_global = cx
                        thumb_cy_global = cy
                        cv2.circle(frame, (cx, cy), 20, (255, 0, 255), cv2.FILLED)
                    if id == 8:
                        pointer_cx_global = cx
                        pointer_cy_global = cy
                        cv2.circle(frame, (cx, cy), 20, (255, 0, 255), cv2.FILLED)
                    if id == 12:
                        middle_cx_global = cx
                        middle_cy_global = cy
                        cv2.circle(frame, (cx, cy), 20, (255, 0, 255), cv2.FILLED)
                        
                        
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
    
            

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    
    
def MoveLight(cxInverse,):
    global cursor_cx_global
    global cursor_cy_global
    global thumb_cx_global
    global thumb_cy_global
    global pointer_cx_global
    global pointer_cy_global
    global middle_cx_global
    global middle_cy_global
    while True:
        print("ydist", pointer_cy_global-thumb_cy_global)
        print("xdist", pointer_cx_global-thumb_cx_global)
        if (pointer_cx_global-thumb_cx_global >= -100 & pointer_cy_global-thumb_cy_global >= -100):
            lightPosFreeze = True
            return

        cxInverse = (cursor_cx_global *-1) + 1920
        if LightPosFreeze:
             # Light.moveTox(cxInverse)
             # Light.moveToy(2*cursor_cy_global)
            return


        
        
if __name__ == '__main__':
    t1 = threading.Thread(target = FindHands,args=(cap,))
    t2 = threading.Thread(target = MoveLight,args=(cxInverse,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    

     