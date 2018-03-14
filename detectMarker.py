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

print("Press ESC to exit")

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedCorners = cv2.aruco.detectMarkers(gray,dictionary, cameraMatrix = camera_matrix, distCoeff = dist_coeff)
    gray = cv2.aruco.drawDetectedMarkers(gray, corners)


    for i in range(len(corners)):
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(corners[i][0][0][0]) + ' x ' + str(corners[i][0][0][1])
        position = (corners[i][0][0][0], corners[i][0][0][1])
        cv2.putText(gray,text , position, font, 0.5,(255,255,255),2,cv2.LINE_AA)

    cv2.namedWindow( 'webcam', cv2.WINDOW_NORMAL );
    cv2.resizeWindow('webcam', 1500, 1200)
    cv2.imshow('webcam', gray, )
    char = cv2.waitKey(25)

    #Write coordinate to file when pressing space
    if char == 32:

        if len(corners) != 3:
            print("Try again, there should be exactly 3 markers in the picture")
            continue

        coordinates = np.asarray([corners[i][0][0] for i in range(len(corners))]).tolist()
        sums = [float(coord[0])+float(coord[1]) for coord in coordinates]
        used = np.ones(len(corners))

        used[np.argmin(sums)] = 0
        yCoord = coordinates[np.argmin(sums)]
        used[np.argmax(sums)] = 0 
        xCoord = coordinates[np.argmax(sums)]
        origo = coordinates[np.argmax(used)]

        print('yCoord: ',yCoord)
        print('xCoord: ',xCoord)
        print('origo: ' , origo)


        data = {'origo': origo, 'xCoord': xCoord, 'yCoord': yCoord}

        with open("coordinates.yaml", "w") as f:
            yaml.dump(data, f)


    # return on esc-press
    if char == 27:
        print("Exiting")
        break
