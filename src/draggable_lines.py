import matplotlib.pyplot as plt
import matplotlib.lines as lines

class DraggableLines:
    def __init__(self, ax, kind, XorY):
        self.ax = ax
        self.c = ax.get_figure().canvas
        self.o = kind
        self.XorY = XorY

        if kind == "h":
            x = [-1, 1]
            y = [XorY, XorY]

        elif kind == "v":
            x = [XorY, XorY]
            y = [-1, 1]
        self.line = lines.Line2D(x, y, picker=True)
        self.ax.add_line(self.line)

        self.sid = self.c.mpl_connect('pick_event', self.clickonline)
        self.c.draw_idle()

    def clickonline(self, event):
        print("entered without artist")
        if event.artist == self.line:
            print("line selected ", event.artist)
            self.follower = self.c.mpl_connect("motion_notify_event", self.followmouse)
            self.releaser = self.c.mpl_connect("button_release_event", self.releaseonclick)
            print("I was clicked")

    def followmouse(self, event):
        print("followmouse entered")
        if self.o == "h":
            self.line.set_ydata([event.ydata, event.ydata])
        else:
            self.line.set_xdata([event.xdata, event.xdata])
        self.c.draw_idle()

    def releaseonclick(self, event):
        if self.o == "h":
            self.XorY = self.line.get_ydata()[0]
        else:
            self.XorY = self.line.get_xdata()[0]

        print (self.XorY)

        self.c.mpl_disconnect(self.releaser)
        self.c.mpl_disconnect(self.follower)

        # update coursor bounds time label
        # update coursor bounds percentage label
        #
        # update coursor bounds list

