import cv2
import ScreenCapture
import ObjectDectection
import numpy as np
import time
import pyautogui
class Fishing:

    def __init__(self):
       pass

    def startFishing(self):
        print("Fishing start enter")
        time.sleep(10)
        od = ObjectDectection.OpjectDectection()
        while (True):
            self.pushFishButton()
            time.sleep(2)
            img = self.getImage()
            top_left = od.findObejctExecuor(img)
            print("top_left = " + str(top_left))
            self.positionCursor(top_left)
            self.waitForBite()

    def pushFishButton(self):
        print("pushFishButtonenter")
        pyautogui.click(button='right')
        time.sleep(0.25)
        pyautogui.click(button='right')
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
        endTime = time.time() + 30
        while True:
            if time.time() >= endTime:
                break
            else:
                if (self.isBite()):
                    pyautogui.click(button='right')
                    break
        pass

    def isBite(self):
#        print("isBite enter")
        return False
        pass

    def positionCursor(self, top_left):
        print("positionCursor enter :" + str(top_left))
        pyautogui.moveTo(top_left[0] + 50 + 500, top_left[1] + 50 + 250, 1.0)
        x, y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        ss = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        ss += ' RGB: (' + str(pixelColor[0]).rjust(3)
        ss += ', ' + str(pixelColor[1]).rjust(3)
        ss += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(ss)
        pass