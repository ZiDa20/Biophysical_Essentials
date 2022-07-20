from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import PySide6 as ps

from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)


class DavesSuperPersonalCustomToolbar(NavigationToolbar):
    def __init__(self, plotCanvas, parent):
        NavigationToolbar.__init__(self, plotCanvas, parent)

        # override _Button() to re-pack the toolbar button in vertical direction

    def _Button(self, text, image_file, toggle, command):
        b = super()._Button(text, image_file, toggle, command)
        print("button type")
        print(type(b))

        #b.pack(side=ps.TOP)  # re-pack button in vertical direction
        return b

        # override _Spacer() to create vertical separator

    def _Spacer(self):
        s = QFrame(self) #, width=26) #, relief=tk.RIDGE, bg="DarkGray", padx=2)
        print(s)
        #s.pack(side=tk.TOP, pady=5)  # pack in vertical direction
        return s

        # disable showing mouse position in toolbar

    def set_message(self, s):
        pass
