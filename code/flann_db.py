import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

FLANN_INDEX_KDTREE = 0

dirs=[
    "dataset/train/5Euro/5eu_front_m.jpg",
    "dataset/train/10Euro/10eu_front_m.jpg",
    "dataset/train/20Euro/20eu_front_m.jpg",
    "dataset/train/50Euro/50eu_front_m.jpg",
    "dataset/train/100Euro/100eu_front_m.jpg",
    "dataset/train/200Euro/200eu_front_m.jpg",
    "dataset/train/500Euro/500eu_front_m.jpg"]

sift = cv2.xfeatures2d.SIFT_create()
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

test=[
    "dataset/test/5__(4).jpg",
    "dataset/test/10__(7).jpg",
    "dataset/test/20__(6).jpg"
]
test=test[2]
img1 = cv2.imread(test,0)

kp1, des1 = sift.detectAndCompute(img1,None)

outputClass=[]
output=[]
for element in dirs:
    outputClass.append(element.split("/")[2])
    img = cv2.imread(element,0)
    print("Detecting and computing" + element)
    kp2, des2 = sift.detectAndCompute(img,None)
    print("Adding...")
    matches = flann.knnMatch(des1,des2,k=2)
    good = 0
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good=good+1
    output.append(good)

print(outputClass)
print(output)