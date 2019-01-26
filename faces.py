#import required libraries 
#import OpenCV library
import cv2

def getFaceList(imgpath):
    cascPath = "haarcascade_frontalface_default.xml"

    test1 = cv2.imread(imgpath)
    gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
    equal_img = cv2.equalizeHist(gray_img)


    faceCascade = cv2.CascadeClassifier(cascPath)

    haar_face_cascade = cv2.CascadeClassifier(cascPath)

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



