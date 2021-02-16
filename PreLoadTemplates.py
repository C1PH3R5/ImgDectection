import cv2
import glob

class PreLoadTemplates:
    templates = []
    def loadTempates(self):
       for file in glob.glob("./data/templates/Test*.jpg"):
           self.templates.append(cv2.imread(file,0))

    def getTemplates(self):
      return self.templates

#      w, h = template.shape[::-1]