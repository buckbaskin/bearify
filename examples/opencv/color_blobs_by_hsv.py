import cv2
import numpy as np

img = cv2.imread('panorama2.jpg')

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

res_array = []

for i in range(0, 179, 20):
    lower_limit = np.array([i,50,50])
    upper_limit = np.array([i+20,205,205])
    mask = cv2.inRange(hsv_img, lower_limit, upper_limit)
    res_array.append(cv2.bitwise_and(img, img, mask=mask))

count = 0
for result in res_array:
    cv2.imshow('img'+str(count),result)
    count += 1

cv2.waitKey(0)
cv2.destroyAllWindows()