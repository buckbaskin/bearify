import cv2
import numpy as np

img = cv2.imread('panorama2.jpg')

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask_array = []
res_array = []

for i in range(0, 179, 20):
    lower_limit = np.array([i,50,50])
    upper_limit = np.array([i+20,205,205])
    mask = cv2.inRange(hsv_img, lower_limit, upper_limit)
    mask_array.append(mask)
    res_array.append(cv2.bitwise_and(img, img, mask=mask))

# for i in range(0,len(mask_array)):
#     cv2.imshow('mask'+str(i),mask_array[i])


# mask 5 is pretty useful

# im = cv2.bitwise_not(mask_array[5])
im = cv2.imread('mask_test1.jpg')
# cv2.imshow('mask 0', im)

im = cv2.blur(im, (5,5))
# cv2.imshow('blur 1', im)

# Set up the detector with default parameters
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.maxArea = 800*600
params.minArea = 10

params.maxThreshold = 200
params.minThreshold = 0

params.filterByConvexity = True
params.minConvexity = .01
params.maxConvexity = 1.0

params.filterByCircularity = True
params.minCircularity = .01
params.maxCircularity = 1.0


detector = cv2.SimpleBlobDetector(params)

# Detect blobs.
keypoints = detector.detect(im)

print(len(keypoints))

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)