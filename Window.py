from tkinter import *
from PIL import ImageTk, Image
import ObjectDectection
import Fishing

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Do it for me")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        startButton = Button(self, text="ScreenCapture", command=self.startObjectDectection)
        captureLoopButton = Button(self, text="ScreenCapture loop", command=self.capturLoopObjectDectection)
        testButton = Button(self, text="Test", command=self.testObjectDectection)
        fishingButton = Button(self, text="Start Fishing", command=self.fishing)
        quitButton = Button(self, text="Exit", command=self.client_exit)

        # placing the button on my window
        startButton.place(x=0, y=0)
        testButton.place(x=120, y=0)
        fishingButton.place(x=165, y=0)
        quitButton.place(x=265, y=0)
        captureLoopButton.place(x=300, y=0)

    def client_exit(self):
        exit()

    def startObjectDectection(self):
        print("startObjectDectection enter")
        od = ObjectDectection.OpjectDectection()
        od.runWhitScreenCapture(self.master)

    def capturLoopObjectDectection(self):
        print("captureLoopObjectDectection enter")
        od = ObjectDectection.OpjectDectection()
        od.runWhitScreenCaptureLoop(self.master)


    def testObjectDectection(self):
        print("testObjectDectection enter")
        od = ObjectDectection.OpjectDectection()
        od.runWhitTestScreens(self.master)

    def fishing(self):
        print("fishing enter")
        fis = Fishing.Fishing()
        fis.startFishing()

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("640x540")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()