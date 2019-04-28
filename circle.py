import cv2
import numpy as np
import random as rnd
import os


def createCircle(self):
    path = "circle"
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)

    for i in range(self):
        rand_circle = rnd.randint(30, 70)
        rand_1 = rnd.randint(rand_circle, 256 - rand_circle)
        rand_2 = rnd.randint(rand_circle, 256 - rand_circle)
        rand_3 = rnd.randint(1, 4)
        img = np.ones((256, 256, 3), np.uint8) * 255
        cv2.circle(img, (rand_1, rand_2), rand_circle, (0, 0, 0), rand_3)
        cv2.imshow("img", img)
        cv2.imwrite("circle/" + str(i) + ".jpg", img)

