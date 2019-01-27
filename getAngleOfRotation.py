import cv2
import numpy as np
#assumes eyelist has 2 eyes

def getAngleOfRotation(eyeList):
    # Calculates the centre of each eye by finding average of corner coordinates
    img1AvgX = eyeList[0][0] + 0.5 * eyeList[0][3]
    img1AvgY = eyeList[0][1] + 0.5 * eyeList[0][4]
    img2AvgX = eyeList[1][0] + 0.5 * eyeList[1][3]
    img2AvgY = eyeList[1][1] + 0.5 * eyeList[1][4]
    #avgCoord = (img1AvgX + img2AvgX / 2, img1AvgY + img2AvgY / 2)

    # Calculates the angle at which the glasses should go
    angleOfRotation = np.arctan((img2AvgX - img1AvgX) / 2, (img2AvgY - img1AvgY) / 2)
    return angleOfRotation
