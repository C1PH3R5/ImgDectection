import datetime
import random

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
 #       print("Fishing start enter")
        time.sleep(10)
        od = ObjectDectection.OpjectDectection()
        while (True):
#            print("1 : " + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-2])
            self.pushFishButton()
#            print("2 : " + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-2])
            time.sleep(self.getRandomBreak())
#            print("3 : " + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-2])
            img = self.getImage(400, 250, 700, 500)
#            print("4 : " + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-2])
            top_left = od.findObejctExecuor(img)
#            print("5 : " + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-2])
            self.positionCursor(top_left)
#            print("6 : " + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-2])
            self.waitForBite(top_left)
#            print("7 : " + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-2])

    def pushFishButton(self):
#        print("pushFishButtonenter : " + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-2])
        pyautogui.click(button='right')
        time.sleep(0.25)
        pyautogui.click(button='right')
#        print("New throw : " + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-2])
        pass

    def getImage(self, x, y, height, wide):
#        print("getImage")
        img = ScreenCapture.ScreenCapture().getScreenshotWholeScreen(x, y, height, wide)
        img_rgb = np.array(img)
        img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        return img
        pass

    def waitForBite(self, top_left):
#        print("waitForBite enter : " + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-2])
        endTime = time.time() + 30
        while True:
            if time.time() >= endTime:
 #               print("no bite timeout : {0}".format(time.asctime(time.localtime())))
                break
            else:
                if (self.isBite(top_left)):
                    pyautogui.click(button='right')
  #                  print("fish to bage : {0}".format(time.asctime(time.localtime())))
                    time.sleep(self.getRandomBreak())
                    break
#        print("waitForBite exit : " + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-2])
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
                if str(pixelColor[0]).rjust(3) == "255" and str(pixelColor[1]).rjust(3) == "255" and str(pixelColor[2]).rjust(3) == "255":
#                    print("it is hooked : " + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-2])
                    return True
                y = y + 1
            x = x + 1
#        print("-- isBite executed %.4f seconds" % ((time.time() - t1)))
        return False
        pass

    def positionCursor(self, top_left):
#        print("positionCursor enter :" + str(top_left))
        pyautogui.moveTo(self.getRealX(top_left[0]) + 50, self.getRealY(top_left[1] + 50), 1.0)
        pass

    def getRealX(self, x):
        return x + 400
        pass

    def getRealY(self, y):
        return y + 250
        pass

    def getRandomBreak(self):
        return random.uniform(2, 5)

        pass