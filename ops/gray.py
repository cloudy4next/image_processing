import numpy as np
import cv2
CODE = 'gray'

class gray:
    def __init__(self):
        self.code = CODE

    def process(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def match_code(code):
        if code == CODE:
            return gray()