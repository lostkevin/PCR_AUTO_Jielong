from listm import idicon
import numpy as np

def similarity(h1, h2, mathc_thres=0.8, ransac_thres=4):
    if min(len(h1[0]), len(h2[0])) <= 1:
        return 0
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(h1[1], h2[1], k=2)
    good = []
    for m, n in matches:
        if m.distance < mathc_thres * n.distance:
            good.append(m)
    if len(good) <= 10:
        return 0
    ptsA = np.float32([h1[0][m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    ptsB = np.float32([h2[0][m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    H, status = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, ransac_thres)
    return str(status).count("1") / len(good)

import cv2
sift = cv2.xfeatures2d.SIFT_create()

def imgHash(img):
    return sift.detectAndCompute(img, None)
