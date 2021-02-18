import cv2
import glob
import ScreenCapture
import PreLoadTemplates
import MajorityDecides

import numpy as np
from matplotlib import pyplot as plt


class OpjectDectection(object, ):
    def __init__(self):
        res_array = np.array(None)

    def FindObejct(self, ):

        preLoadTemplates = PreLoadTemplates.PreLoadTemplates()
        preLoadTemplates.loadTempates()
        templates = preLoadTemplates.getTemplates()

        #        template = cv2.imread('./data/templates/test2.jpg',0)
        #        w, h = template.shape[::-1]

        # All the 6 methods for comparison in a list
        #       methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
        #                   'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        # methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF_NORMED']


        for file in glob.glob("./data/NewBobbels/*.jpg"):
            print(file)
#            img = cv2.imread(file, 0)
            img = ScreenCapture.ScreenCapture().screenshotWholeScreen()
            img_rgb = np.array(img)
            img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

            top_left_array = []
            for template in templates:
                w, h = template.shape[::-1]
                for meth in methods:
#                    img = img2.copy()
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
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(img, top_left, bottom_right, 255, 2)

            plt.imshow(img, cmap='gray')
            plt.title('Detected Point')
            plt.suptitle(file)
            plt.show()

    pass
