import matplotlib.lines as lines
from PySide6.QtCore import *  # type: ignore

class DraggableLines:
    def __init__(self, ax, kind, XorY,canvas, bound_changed, row_number,scaling_factor):
        self.ax = ax
        self.c = canvas
        self.o = kind
        self.XorY = XorY
        self.line = None
        self.scaling_factor = scaling_factor

        self.row_number = row_number
        self.bound_changed = bound_changed

        default_colors = ['k', 'b', 'r', 'g', 'c']

        if kind == "h":
            x = [-1, 1]
            y = [XorY, XorY]

        elif kind == "v":
            x = [XorY, XorY]
            y = [-1*self.scaling_factor, self.scaling_factor]

        self.line = lines.Line2D(x, y, color = default_colors[row_number], picker=True)
        self.ax.add_line(self.line)

        self.sid = self.c.mpl_connect('pick_event', self.clickonline)
        #self.c.draw_idle()

    def clickonline(self, event):
        #print("entered without artist")

        try:
            if event.artist == self.line:
                self.follower = self.c.mpl_connect("motion_notify_event", self.followmouse)
                self.releaser = self.c.mpl_connect("button_release_event", self.releaseonclick)

        except Exception as e:
            #print("Might be possible that there is no artist object in the event .. but code will not be stopped from executing. ")
            #print(e)
            print("click")


    def followmouse(self, event):
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

        self.c.mpl_disconnect(self.releaser)
        self.c.mpl_disconnect(self.follower)

        emit_tuple = (round(self.XorY, 2), self.row_number)
        print(emit_tuple)
        self.bound_changed.cursor_bound_signal.emit(emit_tuple)

