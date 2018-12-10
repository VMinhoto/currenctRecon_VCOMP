import numpy as np
import cv2
import os

import pickle
from urllib import request
import ssl

def classify(url):

    dirs=[
    "dataset/train/5Euro/5eu_front_m.jpg",
    "dataset/train/10Euro/10eu_front_m.jpg",
    "dataset/train/20Euro/20eu_front_m.jpg",
    "dataset/train/50Euro/50eu_front_m.jpg",
    "dataset/train/100Euro/100eu_front_m.jpg",
    "dataset/train/200Euro/200eu_front_m.jpg",
    "dataset/train/500Euro/500eu_front_m.jpg"]

    ssl._create_default_https_context = ssl._create_unverified_context
    resp = request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    img1 = cv2.imdecode(image, 0)
    


    FLANN_INDEX_KDTREE = 0

    sift = cv2.xfeatures2d.SIFT_create()
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)



    kp1, des1 = sift.detectAndCompute(img1,None)

    output=[]
    for element in dirs:
        img2=cv2.imread("/Users/vitorminhoto/Documents/gitHub/currencyRecon_VCOMP/dataset/"+element,0)
        kp2, des2 = sift.detectAndCompute(img2,None)
        matches = flann.knnMatch(des1,des2,k=2)
        good = 0
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good=good+1
        output.append(good)
    number=np.argmax(output)
    

    return dirs[number].split("/")[2]
        
#a=classify("https://scontent.xx.fbcdn.net/v/t1.15752-9/47400476_214206709493398_374042383911747584_n.jpg?_nc_cat=103&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=d656aaafb912fb8b1dfb5345f4f3d997&oe=5CB1822C")
#print(a)
