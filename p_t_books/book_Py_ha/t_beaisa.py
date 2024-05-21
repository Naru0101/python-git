import sys
import random
import itertools
import numpy as np
import cv2 as cv

map_file = 'cape_python.png'

sa1_conners = (130, 265, 180, 315) # (UL-X, UL-Y, LR-X, LR-Y)
sa2_conners = (80, 255, 130, 305) # (UL-X, UL-Y, LR-X, LR-Y)
sa3_conners = (105, 205, 155, 255) # (UL-X, UL-Y, LR-X, LR-Y)

class Search():
    """Байесовская игра "Поиск и спасение" с 3 областями поиска."""

    def __init__(self, name):
        self.name = name
        self.img = cv.imread(map_file, cv.imread_color)
        if self.img is None:
            print("Could not load map file {}".format(map_file),
                  file=sys.stderr)
            sys.exit(1)

        self.area_actual = 0
        self.sailor_actual = [0,0] # cordinat the 'local'
        self.sa1 = self.img[sa1_corners[1] : sa1_corners[3],
                            sa1_corners[0] : sa1_corners[2]]

        self.sa2 = self.img[sa2_corners[1] : sa2_corners[3],
                            sa2_corners[0] : sa2_corners[2]]self.sa1 = self.img[sa1_corners[1] : sa1_corners[3],

        self.sa3 = self.img[sa3_corners[1] : sa3_corners[3],
                            sa3_corners[0] : sa3_corners[2]]

        self.p1 = 0.2
        self.p2 = 0.5
        self.p3 = 0.3
                                                                                
        self.sep1 = 0
        self.sep2 = 0
        self.sep3 = 0










                                                                                
