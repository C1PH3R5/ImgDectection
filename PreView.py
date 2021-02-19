from matplotlib import pyplot as plt

class PreView:
    # Define settings upon initialization. Here you can specify
    def __init__(self):
        pass

    def showPreView(self, img, sec):
        plt.imshow(img, cmap='gray')
        plt.title('Detected Point')
        plt.suptitle("Preview in " + str(sec) + " sec")
        plt.show(block=False)
        plt.pause(sec)
        plt.close()