# import the necessary packages
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# construct the argument parser to parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help="Path to the img")
args = vars( ap.parse_args() )

# load the img and show it
image = cv2.imread( args["image"] ) 
cv2.imshow("image", image)

# convert the img to grayscale and create a histogram
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Histograma Cinza")
plt.xlabel("Bins")
plt.ylabel("num of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
