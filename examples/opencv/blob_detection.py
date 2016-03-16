# Standard imports
import cv2
import numpy as np;
 
# Read image
im = cv2.imread("blob2.jpg")
 
# Set up the detector with default parameters.
params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 240
params.maxThreshold = 255

params.filterByArea = True
params.minArea = 1500

detector = cv2.SimpleBlobDetector(params)
 
# Detect blobs.
keypoints = detector.detect(im)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)