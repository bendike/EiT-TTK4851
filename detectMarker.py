import cv2
import numpy as np
import yaml

with open('calibration.yaml') as f:
    loadeddict = yaml.load(f)
mtx = loadeddict.get('camera_matrix')
dist = loadeddict.get('dist_coeff')

camera_matrix = np.asarray(mtx)
dist_coeff = np.asarray(dist)

cap = cv2.VideoCapture(0)
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedCorners = cv2.aruco.detectMarkers(gray,dictionary, cameraMatrix = camera_matrix, distCoeff = dist_coeff)
    gray	=	cv2.aruco.drawDetectedMarkers(gray, corners)
    cv2.namedWindow( 'webcam', cv2.WINDOW_NORMAL );
    cv2.resizeWindow('webcam', 1500,1200)
    cv2.imshow('webcam', gray, )
    char = cv2.waitKey(25)

    # return on esc-press
    if char == 27:
        print("Exiting")
        break
