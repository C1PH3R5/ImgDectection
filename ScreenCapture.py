import numpy as np
import cv2 as cv
import time
import pyautogui



class ScreenCapture:

    def __init__(self):
        self.output = np.array("", )
        self.img = None

    def getScreenshotWholeScreen(self, x, y, height, wide):
        screenshot = self.getScreenShotScreen(x, y, height, wide)
        screenshot = np.array(screenshot)
        screenshot = screenshot[:, :, ::-1].copy()
        return(screenshot)

    def getScreenShotScreen(self, x, y, height, wide):
        screenshot = pyautogui.screenshot(region=(x, y, height, wide))
        return screenshot