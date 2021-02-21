import cv2
import glob
import ScreenCapture
import PreLoadTemplates
import MajorityDecides
import PreView

import numpy as np

class OpjectDectection(object):
    def __init__(self):
        self.preLoadTemplates = PreLoadTemplates.PreLoadTemplates()
        self.preLoadTemplates.loadTempates()
        self.templates = self.preLoadTemplates.getTemplates()
        self.methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF_NORMED']
        pass

    def runWhitScreenCapture(self, window):
        print("runWhitScreenCapture enter")
        img = ScreenCapture.ScreenCapture().screenshotWholeScreen()
        img_rgb = np.array(img)
        img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        img = self.testFindObejct(img, window)

    def runWhitTestScreens(self, window):
        for file in glob.glob("./data/NewBobbels/*.jpg"):
            print(file)
            img = cv2.imread(file, 0)
            img = self.testFindObejct(img, window)

    def testFindObejct(self, img, window):
        top_left = self.FindObejct(img)
#        w, h = template.shape[::-1]
        w = 100
        h = 100

        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img, top_left, bottom_right, 255, 2)

        pv = PreView.PreView()
        pv.showPreView(img, window)

        return img

    def FindObejct(self, img):

        top_left_array = []
        for template in self.templates:
            for meth in self.methods:
                method = eval(meth)

                # Apply template Matching
                res = cv2.matchTemplate(img, template, method)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

                # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
                if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                    top_left = min_loc
                else:
                    top_left = max_loc
                top_left_array.append(top_left)

        majorityDecides = MajorityDecides.MajorityDecides()
        top_left = majorityDecides.mostCommon(top_left_array)
        return top_left

    pass
