import cv2

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

for i in range(0,50):
    marker = cv2.aruco.drawMarker(dictionary, i, 500)
    filename = "marker_" + str(i) + ".png"
    cv2.imwrite(filename, marker)
    print("Marker: ", i)
    char = cv2.waitKey(750)

cv2.destroyAllWindows()
