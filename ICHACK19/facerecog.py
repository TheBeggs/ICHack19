from __future__ import print_function
import cv2 as cv
import time

level_map = [(0,0,10,10)]
glasses = cv.imread("glasses.png", cv.IMREAD_UNCHANGED);

def detectAndDisplay(frame):
    
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray) #Equalises the histogram -> Increases contrast
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
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
            
            #print(eyes)


            if (((x2 - x1)/glasses.shape[1]) > 0 and ((y2 - y1)/glasses.shape[0]) > 0):
                pic = cv.resize(glasses, (0,0) , fx = ((x2 - x1)/glasses.shape[1]), fy = (y2 - y1)/glasses.shape[0])
                    

                # channels[4]
            

                
                #print(pic.shape)
                #print(frame.shape)
                alpha = pic[:, :, 3] / 255.0
                beta = 1.0 - alpha
                hooray = pic[:, :, :3]
                #frame[y +y1: y +y2, x + x1: x + x2] = pic
                #frame[y +y1: y +y2, x + x1: x + x2, 2] / 255.0

                for c in range(0, 3):
                    frame[y + y1: y+ y2, x+ x1:x+ x2, c] = alpha * hooray[:,:,c] + beta * frame[y+y1:y+y2, x+x1:x+x2, c]
            
            #frame[y +y2:y +y2 + star.shape[0], x+ x2:x +x2 + star.shape[1]] = star
        """
        for (x2,y2,w2,h2) in eyes:
            
            star = cv.resize(star_image, (0,0), fx=w2/star_image.shape[1], fy= h2/star_image.shape[0])
            frame[y +y2:y +y2 + star.shape[0], x+ x2:x +x2 + star.shape[1]] = star

            #frame[y +y2:y +y2 + star.shape[0], x+ x2:x +x2 + star.shape[1]] = star

            #for block in level_ap
            
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
        """
    return frame

"""  
parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera devide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
"""

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
eyes_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")


"""
#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile("haarcascade_frontalface_alt.xml")):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile('haarcascade_eye_tree_eyeglasses.xml')):
    print('--(!)Error loading eyes cascade')
    exit(0)
"""
    
#-- 2. Read the video stream
cap = cv.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
cap.set(5, 30)

count = 0;

if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while (True):
    now = time.time()
    
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break

    newFrame = detectAndDisplay(frame)
    cv.imshow('Glasses Gang', frame)
    
    if cv.waitKey(1) == 27:
        break

    elapsed = time.time() - now  # how long was it running?
    while(1/30 > elapsed):
        elapsed = time.time() - now

    
cap.release()
