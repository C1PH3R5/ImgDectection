import numpy as np
import cv2 as cv
import time
import pyautogui



class ScreenCapture:

    def __init__(self):
        self.output = np.array("", )
        self.img = None
        self.loopTime = 0

    def screenshotWholeScreen(self):
        while (True):
            screenshot = pyautogui.screenshot()
            screenshot = np.array(screenshot)
            screenshot = screenshot[:, :, ::-1].copy()

            cv.imshow('Computer stream', screenshot)
            

            print('FPS {}'.format(1 / (time.time() - self.loopTime)))
            self.loopTime = time.time()

            if cv.waitKey(1) == ord('q'):
                break
        cv.destroyAllWindows()
        print("Done.")
        return(screenshot)
            
