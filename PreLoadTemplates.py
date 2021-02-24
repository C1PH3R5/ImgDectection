import cv2
import glob

class PreLoadTemplates:
    templates = []
    def loadTempates(self):
       self.templates.clear()
       for file in glob.glob("./data/NewBobbels/BobbleRrpo/items/*.jpg"):
           self.templates.append(cv2.imread(file,0))

    def getTemplates(self):
      return self.templates

#      w, h = template.shape[::-1]