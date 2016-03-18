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

# find blobs in all the images!
# Set up the detector with default parameters
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.maxArea = 800*600
params.minArea = (500+750)/4

params.maxThreshold = 200
params.minThreshold = 0

params.filterByConvexity = True
params.minConvexity = .01
params.maxConvexity = 1.0

params.filterByCircularity = True
params.minCircularity = .01
params.maxCircularity = 1.0


detector = cv2.SimpleBlobDetector(params)

keypoints_sum = 0

for i in range(0,len(mask_array)):
    # cv2.imshow('mask'+str(i),mask_array[i])
    im = cv2.bitwise_not(mask_array[i])
    keypoints = detector.detect(im)
    keypoints_sum += len(keypoints)
    cv2.imshow('cut image '+str(i), res_array[i])
    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('Keypoints '+str(i), im_with_keypoints)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print('keypoints_sum '+str(keypoints_sum))