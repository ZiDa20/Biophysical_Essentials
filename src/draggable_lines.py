import matplotlib.lines as lines
from PySide6.QtCore import *  # type: ignore

class DraggableLines:
    def __init__(self, ax, kind, XorY,canvas, bound_changed, row_column_tuple,scaling_factor):
        self.ax = ax
        self.c = canvas
        self.o = kind
        self.XorY = XorY
        self.line = None
        self.scaling_factor = scaling_factor

        self.button_number = row_column_tuple[0]
        self.table_column = row_column_tuple[1]


        self.bound_changed = bound_changed

        default_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']
        if kind == "h":
            x = [-1, 1]
            y = [XorY, XorY]

        elif kind == "v":
            x = [XorY, XorY]

            if isinstance(self.scaling_factor,tuple):
               y = [self.scaling_factor[0],self.scaling_factor[1]] 
            else:
               y = [-1*self.scaling_factor, self.scaling_factor]

        self.line = lines.Line2D(x, y, color = default_colors[row_column_tuple[0]+row_column_tuple[1]], picker=True)

        self.draw_line_on_ax(self.ax)      

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

        emit_tuple = (round(self.XorY, 2),  self.button_number, self.table_column )
        print(emit_tuple)
        self.bound_changed.cursor_bound_signal.emit(emit_tuple)

    def redraw(self):
        #self.line = lines.Line2D(x, y, color = default_colors[row_column_tuple[0]+row_column_tuple[1]], picker=True)
        self.ax.add_line(self.line)
        self.sid = self.c.mpl_connect('pick_event', self.clickonline)

    def draw_line_on_ax(self,ax):
         ax.add_line(self.line)
    