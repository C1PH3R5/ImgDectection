from matplotlib import pyplot as plt
from tkinter import *
from PIL import ImageTk, Image


class PreView:
    # Define settings upon initialization. Here you can specify
    def __init__(self):
        pass

    def showPreView(self, img, window):

        pil_image = Image.fromarray(img)
        pil_image = pil_image.resize((600,  400), Image.ANTIALIAS)
        imgTK = ImageTk.PhotoImage(pil_image)
        canvas = Canvas(window, width=620, height=420)
        canvas.create_image(20, 20, anchor=NW, image=imgTK)
        canvas.image = imgTK
        canvas.place(x=0, y=100)
        canvas.update()
