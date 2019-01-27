from __future__ import print_function
import cv2 as cv
import numpy as np

src = cv.imread("canT.jpg", cv.IMREAD_GRAYSCALE)
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)
#-- Step 1: Detect the keypoints using SURF Detector
minHessian = 400
detector = cv.xfeatures2d_SURF.create(hessianThreshold=minHessian)
keypoints = detector.detect(src)
#-- Draw keypoints
img_keypoints = np.empty((src.shape[0], src.shape[1], 3), dtype=np.uint8)
cv.drawKeypoints(src, keypoints, img_keypoints)
#-- Show detected (drawn) keypoints
cv.imshow('SURF Keypoints', img_keypoints)
cv.waitKey()
