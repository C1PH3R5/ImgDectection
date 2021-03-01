from tkinter import *
from tkinter.font import Font

from PIL import ImageTk, Image
import ObjectDectection
import Fishing

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    width: object
    height: object

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.root = None
        self.master = master
        self.frame = None
        self.frameImg = None
        self.canvas = None
        self.width = None
        self.height = None
        self.screenShootTopLeft = None
        self.screenShootWidth = None
        self.screenShootHeight = None
        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Do it for me")
        Grid.rowconfigure(self.master, index=0, weight=1)
        Grid.rowconfigure(self.master, index=1, weight=30)
        Grid.columnconfigure(self.master, index=0, weight=1)


        self.frame = Frame(self.master, borderwidth=5, relief="ridge", width=640, height=540)
        Grid.rowconfigure(self.frame, index=0, weight=1)
        Grid.columnconfigure(self.frame, index=0, weight=1)
        Grid.columnconfigure(self.frame, index=1, weight=1)
        Grid.columnconfigure(self.frame, index=2, weight=1)
        Grid.columnconfigure(self.frame, index=3, weight=1)
        Grid.columnconfigure(self.frame, index=4, weight=1)

        self.frameImg = Frame(self.master, borderwidth=5, relief="ridge", width=640, height=540)
        Grid.rowconfigure(self.frameImg, index=0, weight=1)
        Grid.columnconfigure(self.frameImg, index=0, weight=1)


        self.canvas = Canvas(self.frameImg, width=620, height=420)
        self.canvas.grid(column=0, row=0, sticky="nsew")
        self.canvas.bind("<Configure>", self.resize)
        Grid.rowconfigure(self.canvas, index=0, weight=1)
        Grid.columnconfigure(self.canvas, index=0, weight=1)


        startButton = Button(self.frame, text="ScreenCapture", command=self.startObjectDectection)
        captureLoopButton = Button(self.frame, text="ScreenCapture loop", command=self.capturLoopObjectDectection)
        testButton = Button(self.frame, text="Test", command=self.testObjectDectection)
        fishingButton = Button(self.frame, text="Start Fishing", command=self.fishing)
        quitButton = Button(self.frame, text="Exit", command=self.client_exit)

        self.frame.grid(column=0, row=0, sticky="ew")
        self.frameImg.grid(column=0, row=1, sticky="nsew")

        startButton.grid(column=0, row=0, sticky="ew")
        testButton.grid(column=1, row=0, sticky="ew")
        fishingButton.grid(column=2, row=0, sticky="ew")
        captureLoopButton.grid(column=3, row=0, sticky="ew")
        quitButton.grid(column=4, row=0, sticky="ew")

        myFont = Font(size=12)
        startButton["font"] = myFont
        testButton["font"] = myFont
        fishingButton["font"] = myFont
        captureLoopButton["font"] = myFont
        quitButton["font"] = myFont

        midelOfScreen = self.findMidelOfScreen()
        print(str(midelOfScreen[0]))
        print(str(midelOfScreen[1]))

        self.screenShootWidth = self.findScreenShootWidth()
        print(str(self.screenShootWidth))

        self.screenShootHeight = self.findScreenShootHeight()
        print(str(self.screenShootHeight))

        self.screenShootTopLeft = self.findScreenShootTopLeft(midelOfScreen, self.screenShootWidth, self.screenShootHeight)
        print(str(self.screenShootTopLeft))

    def showImg(self, img):
        pil_image = Image.fromarray(img)
        pil_image = pil_image.resize((self.width, self.height), Image.ANTIALIAS)
        imgTK = ImageTk.PhotoImage(pil_image)

        self.canvas.create_image(20, 20, anchor=NW, image=imgTK)
        self.canvas.image = imgTK
        self.canvas.update()
        pass

    def getScreenShootTopLeft(self):
        return self.screenShootTopLeft

    def getScreenShootWidth(self):
        return self.screenShootWidth

    def getScreenShootHeight(self):
        return self.screenShootHeight

    def resize(self, event):
        self.width = event.width
        self.height = event.height

    def client_exit(self):
        exit()

    def startObjectDectection(self):
        print("startObjectDectection enter")
        od = ObjectDectection.OpjectDectection()
        od.runWhitScreenCapture(self)

    def capturLoopObjectDectection(self):
        print("captureLoopObjectDectection enter")
        od = ObjectDectection.OpjectDectection()
        od.runWhitScreenCaptureLoop(self)


    def testObjectDectection(self):
        print("testObjectDectection enter")
        od = ObjectDectection.OpjectDectection()
        od.runWhitTestScreens(self)

    def fishing(self):
        print("fishing enter")
        fis = Fishing.Fishing()
        fis.startFishing(self)

    def findMidelOfScreen(self):
        w = int(self.winfo_screenwidth() / 2)
        h = int(self.winfo_screenheight() / 2)
        print("winfo_width : " + str(w))
        print("winfo_height : " + str(h))
        return [w, h]

    def findScreenShootWidth(self):
        w = self.winfo_screenwidth()
        return int(w * 33.3 / 100)

    def findScreenShootHeight(self):
        h = self.winfo_screenheight()
        return int(h * 60 / 100)

    def findScreenShootTopLeft(self, midelOfScreen, screenShootWidth, screenShootHeight):
        x = int(midelOfScreen[0] - (screenShootWidth / 2))
        y = int(midelOfScreen[1] - (screenShootHeight / 2))
        return [x, y]

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

app = Window(root)

# mainloop
root.mainloop()