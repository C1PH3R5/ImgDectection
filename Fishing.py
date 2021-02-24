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
            img = self.getImage(500, 250, 700, 500)
            top_left = od.findObejctExecuor(img)
            print("top_left = " + str(top_left))
            self.positionCursor(top_left)
            self.waitForBite(top_left)

    def pushFishButton(self):
        print("pushFishButtonenter")
        pyautogui.click(button='right')
        time.sleep(0.25)
        pyautogui.click(button='right')
        pass

    def getImage(self, x, y, height, wide):
        print("getImage")
        img = ScreenCapture.ScreenCapture().getScreenshotWholeScreen(x, y, height, wide)
        img_rgb = np.array(img)
        img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        return img
        pass

    def waitForBite(self, top_left):
        print("waitForBite enter")
        endTime = time.time() + 30
        while True:
            if time.time() >= endTime:
                break
            else:
                if (self.isBite(top_left)):
                    pyautogui.click(button='right')
                    break
        pass

    def isBite(self, top_left):
        t1 = time.time()
        xMax = 75
        yMax = 75
        img = ScreenCapture.ScreenCapture().getScreenShotScreen(self.getRealX(top_left[0]), self.getRealY(top_left[1]), xMax, yMax)
        x = 1
        # rgb(255, 255, 255)
        while (x < xMax):
            y = 1
            while (y < yMax):
                pixelColor = img.getpixel((x, y))
                if str(pixelColor[0]).rjust(3) == "255" and str(pixelColor[1]).rjust(3) == "255" and str(pixelColor[2]).rjust(3) == "255" :
                    return True
                y = y + 1
            x = x + 1
#        print("-- isBite executed %.4f seconds" % ((time.time() - t1)))
        return False
        pass

    def positionCursor(self, top_left):
        print("positionCursor enter :" + str(top_left))
        pyautogui.moveTo(self.getRealX(top_left[0]) + 50, self.getRealY(top_left[1] + 50), 1.0)
        pass

    def getRealX(self, x):
        return x + 500
        pass

    def getRealY(self, y):
        return y + 250
        pass