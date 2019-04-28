
import numpy as np
import cv2
import random as rnd
import os


def createDiamonds(self):
    path = "diamond"
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)

    for i in range(self):
        rand = rnd.randint(0, 100)
        rand_thick = rnd.randint(1, 4)
        img = np.ones((256, 256, 3), dtype="uint8") * 255
        pts = np.array(
            [[50 + rand, 0 + rand], [100 + rand, 50 + rand], [50 + rand, 100 + rand], [0 + rand, 50 + rand]],
            np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 0, 0), rand_thick)
        cv2.imwrite("diamond/"+str(i)+".jpg",img)