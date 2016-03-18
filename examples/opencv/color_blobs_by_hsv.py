'''
TODO:
- separate out gray/silver from colors
- ignore bright whites (in HSV not blobs)

- make overlapping color sets (range of 20, step of 10 kind of thing)
- combine keypoints for nearby color sets (i.e. a blob is detected twice as two
    closeish colors)
- make a wrapping red color set (2 masks, bitwise or)

- Check the effects of blurring image first
    - blurring the image first creates a number of blobs that seem closer to my
        sense of what areas should be blobs
- Check the effects of blurring the masks (non-blurred image)
    - blurring the masks tends to group more points, but in some cases it splits
        up blobs that would otherwise have been together.
'''

import cv2
import numpy as np

img = cv2.imread('panorama2.jpg')
# img = cv2.blur(img, (5,5,))

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
params.minArea = 300

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
    im = cv2.blur(cv2.bitwise_not(mask_array[i]), (5,5,))
    keypoints = detector.detect(im)
    keypoints_sum += len(keypoints)
    cv2.imshow('cut image '+str(i), res_array[i])
    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('Keypoints '+str(i), im_with_keypoints)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print('keypoints_sum '+str(keypoints_sum))