import cv2
import numpy as np
import yaml

with open('calibration.yaml') as f:
    loadeddict = yaml.load(f)
mtx = loadeddict.get('camera_matrix')
dist = loadeddict.get('dist_coeff')
rvecs = loadeddict.get('rvecs')
tvecs = loadeddict.get('tvecs')
