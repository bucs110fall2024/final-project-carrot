class Window:
    def __init__(self, x, y, h, w):
        """
        Creates a window to display infor
        Args:
            x (int): x coord
            y (int): y coord
            h (int): height
            w (int): width
        """
        self.xWindow = x
        self.yWindow = y
        self.windowHeight = h
        self.windowWidth = w
        
    def closeWindow(self):
        """
        Closes the window upon user clicking the the exit button
        args: none
        returns: none
        """