#import required libraries 
#import OpenCV library
import cv2

def getFaceList(imgpath):
    cascPath = "haarcascade_frontalface_default.xml"

    test1 = cv2.imread(imgpath)
    gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
    equal_img = cv2.equalizeHist(gray_img)


    faceCascade = cv2.CascadeClassifier(cascPath)


    faces = faceCascade.detectMultiScale(
        equal_img,
        scaleFactor=1.1,
        minNeighbors=5
    )

    print("Found {0} faces!".format(len(faces)))

    croppedfaces = []

    for (x, y, w, h) in faces:
        croppedfaces.append(test1[y:y+h,x:x+w])

    return croppedfaces

def getEyeList(face):
    cascPath = "haarcascade_eyes.xml"
    grayFace = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    eyeCascade = cv2.CascadeClassifier(cascPath)
    eyes = eyeCascade.detectMultiScale(grayFace)

    croppedeyes = []
    
    for (ex,ey,ew,eh) in eyes:
        croppedeyes.append(face[y:y+h,x:x+w])      
    

    return croppedeyes
