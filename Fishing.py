import cv2
import ScreenCapture
import ObjectDectection
import numpy as np
import datetime
import time
class Fishing:

    def __init__(self):
       pass

    def startFishing(self):
        print("Fishing start enter")
        od = ObjectDectection.OpjectDectection()
        while (True):
            self.pushFishButton()
            img = self.getImage()
            top_left = od.FindObejct(img)
            print("top_left = " + str(top_left))
            self.waitForBite()

    def pushFishButton(self):
        print("pushFishButtonenter")
        pass

    def getImage(self):
        print("getImage")
        img = ScreenCapture.ScreenCapture().screenshotWholeScreen()
        img_rgb = np.array(img)
        img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        return img
        pass

    def waitForBite(self):
        print("waitForBite enter")
        endTime = time.time() + 5
        while True:
            if time.time() >= endTime:
                break
            else:
                if (self.isBite()):
                    break
        pass

    def isBite(self):
#        print("isBite enter")
        return False
        pass