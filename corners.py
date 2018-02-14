import cv2
import numpy as np

filename = 'export.png'
img = cv2.imread(filename, 1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# img32 = np.float32(img)
# img = cv2.cornerHarris(img32,2,3,0.07)
# img = cv2.dilate(img,None)
# img = cv2.resize(img, (960, 960))
cv2.imshow('rgb',img)
cv2.imshow('hsv',hsv)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
