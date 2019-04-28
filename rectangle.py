import cv2
import numpy as np
import random as rnd
import os


def createRectangle(self):
    path = "rectangle"
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)

    for i in range(self):
        rand_rectangle_1 = rnd.randint(0, 90)
        rand_1 = rnd.randint(rand_rectangle_1 + 38, 256 - rand_rectangle_1 - 2)
        rand_2 = rnd.randint(1, 4)
        img = np.ones((256, 256, 3), np.uint8) * 255
        cv2.rectangle(img, (rand_rectangle_1, rand_rectangle_1 + rand_rectangle_1),
                      (rand_1 + rand_rectangle_1, rand_1 + rand_rectangle_1), (0, 0, 0), rand_2)
        cv2.imwrite("rectangle/" + str(i) + ".jpg", img)
