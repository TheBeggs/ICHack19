from __future__ import print_function
import cv2 as cv
import time
import random
import os


def detectAndDisplay(frame, hatBool, glassesBool, glasses, hat):
    
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray) #Equalises the histogram -> Increases contrast
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        if (hatBool):
            top = y - 4 * (h//5)
            hatResize = cv.resize(hat, (0,0), fx = w/hat.shape[1] , fy = w/hat.shape[0])
            alpha1 = hatResize[:, :, 3] / 255.0
            beta1 = 1.0 - alpha1
            RGBHat = hatResize[:,:,:3]

            if (top > 0 and hatResize.shape[0] != 0) :
                for c in range(0, 3):
                    frame[top:top+hatResize.shape[0], x:x+hatResize.shape[1], c] = alpha1 * RGBHat[:,:,c] + beta1 * frame[top:top+hatResize.shape[0], x:x+hatResize.shape[1], c]
            else:
                for c in range(0, 3):
                    frame[0:top+hatResize.shape[0], x:x+hatResize.shape[1], c] = alpha1[top * -1:,:] * hatResize[top * -1:, :, c] + beta1[top * -1:,:] * frame[0:top+hatResize.shape[0], x:x+hatResize.shape[1], c]
        
        if (glassesBool):
            faceROI = frame_gray[y:y+h,x:x+w]
            #-- In each face, detect eyes
            eyes = eyes_cascade.detectMultiScale(faceROI)

            if len(eyes) == 2:
                if eyes[0][0] > eyes[1][0]:
                    left = eyes[0]
                    right = eyes[1]
                else:
                    left = eyes[1]
                    right = eyes[0]
                x1 = right[0]
                x2 = left[0] + left[2]                
                x1 -= (x2 - x1)//4
                x2 += (x2 - x1)//4
                y1 = right[1]
                y2 = left[1] + left[3]
                y2 += (y2 - y1)//2

                if (((x2 - x1)/glasses.shape[1]) > 0 and ((y2 - y1)/glasses.shape[0]) > 0):
                    pic = cv.resize(glasses, (0,0) , fx = ((x2 - x1)/glasses.shape[1]), fy = (y2 - y1)/glasses.shape[0])
                    alpha = pic[:, :, 3] / 255.0
                    beta = 1.0 - alpha
                    hooray = pic[:, :, :3]
                    for c in range(0, 3):
                        frame[y + y1: y+ y2, x+ x1:x+ x2, c] = alpha * hooray[:,:,c] + beta * frame[y+y1:y+y2, x+x1:x+x2, c]
    return frame

#liveFilters(True, True, "hair.png", "glasses.png")
def liveFilters(hatBool, glassesBool, hatPath, glassesPath):

    global face_cascade;
    face_cascade = cv.CascadeClassifier("Classifiers/haarcascade_frontalface_alt.xml")
    global eyes_cascade;
    eyes_cascade = cv.CascadeClassifier("Classifiers/haarcascade_eye_tree_eyeglasses.xml")
    

    hat     = cv.imread(hatPath, cv.IMREAD_UNCHANGED)
    glasses = cv.imread(glassesPath, cv.IMREAD_UNCHANGED)

    #-- 2. Read the video stream
    cap = cv.VideoCapture(0)
    cap.set(3, 1920)
    cap.set(4, 1080)
    cap.set(5, 30)

    count = 0;

    if not cap.isOpened:
        print('--(!)Oops opening video capture')
        exit(0)
    while (True):
        now = time.time()
        
        ret, frame = cap.read()
        if frame is None:
            print('--(!) No captured frame -- Break!')
            break

        newFrame = detectAndDisplay(frame, hatBool, glassesBool, glasses, hat)
        cv.imshow('Glasses Gang', frame)
        
        keypress = cv.waitKey(1)
        if keypress == 27:
            break
        elif keypress == 112:
            cv.imshow("Photo",newFrame)


            name = "My Pictures/picture"
            filenumber = 0
            while(True):
                filename = name + str(filenumber) + ".jpg"
                if (not os.path.isfile(filename)):
                    break
                filenumber += 1

            
            cv.imwrite(filename, newFrame)
        

        elapsed = time.time() - now  # how long was it running?
        while(1/60 > elapsed):
            elapsed = time.time() - now
    cap.release()
    cv.destroyAllWindows()
    menu.run()

def stillFilters(hatBool, glassesBool, hatPath, glassesPath, picturePath):
    print("YOOOOOOOO!")
    global face_cascade;
    face_cascade = cv.CascadeClassifier("Classifiers/haarcascade_frontalface_alt.xml")
    global eyes_cascade;
    eyes_cascade = cv.CascadeClassifier("Classifiers/haarcascade_eye_tree_eyeglasses.xml")
    hat     = cv.imread(hatPath, cv.IMREAD_UNCHANGED)
    glasses = cv.imread(glassesPath, cv.IMREAD_UNCHANGED)

    img = cv.imread(picturePath)
    newImg = detectAndDisplay(img,hatBool, glassesBool, glasses, hat)
    name = "My Pictures/picture"
    filenumber = 0
    while(True):
        filename = name + str(filenumber) + ".jpg"
        if (not os.path.isfile(filename)):
             break
        filenumber += 1

            
    cv.imwrite(filename, newImg)
    cv.imshow('Output Image', newImg)
    cv.waitKey(0) 
    cv.destroyAllWindows()
    menu.run()
    

