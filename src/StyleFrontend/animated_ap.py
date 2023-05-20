import matplotlib
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation

class LoadingAnimation:
    def __init__(self, message, frontend_style, progress_bar_enabled = False, parent = None):
        """_summary_
        """
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedWidth(250)
        self.progress_bar.setAlignment(Qt.AlignLeft)
        self.wait_widget = QWidget()
        if parent:
            self.wait_widget_layout = QGridLayout(parent)
        else:
            self.wait_widget_layout = QGridLayout()
        self.new_label = QLabel()
        self.new_label.setText(message)
        self.font = QFont()
        self.font.setPointSize(25)
        self.new_label.setFont(self.font)
        self.new_label.setAlignment(Qt.AlignCenter)
        self.wait_widget_layout.addWidget(self.new_label,0, 0, 1, 3)
        self.canvas_widget = QWidget()
        self.wait_widget_layout.addWidget(self.canvas_widget,1,1)
        # that the style sheet for the plot class

        if frontend_style.default_mode == 0:
            frontend_style.set_mpl_style_dark()
            self.draw_color = "white"
            self.ax_color = "white"
        else:
            frontend_style.set_mpl_style_white()
            self.draw_color = "black"
            self.ax_color = "black"

        #self.wait_widget_layout.setAlignment(Qt.AlignCenter)
        self.fig = Figure(figsize=(2,2))
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.canvas_widget)
        self.time = None
        self.potential = None
        self.status_label = QLabel("Processing ...") #The File is currently not loaded
        self.status_label.setAlignment(Qt.AlignCenter)
        self.font.setPointSize(12)
        self.wait_widget_layout.addWidget(self.status_label,3,1)
        #wait_widget_layout.addWidget(statusbar,3,0)
        if progress_bar_enabled:
            self.wait_widget_layout.addWidget(self.progress_bar,2,1)
        self.wait_widget.setLayout(self.wait_widget_layout)
        self.create_ap_line_out()
        self.start_animation_timer()
    

    def create_ap_line_out(self):
        """Creates the outline of the action potential based on some artifical
        values at different membrane potentials

        """
         # Create a plot on the figure
        self.ax = self.fig.add_subplot(111)
        matplotlib.rcParams['toolbar'] = 'None'
        # Define the time points at which the action potential will be sampled
        self.time = [0, 1, 2, 3, 4, 5,6,7,8,9,10]
        # Define the values of the action potential at each time point
        self.potential = [-60, -59, -53, -50,-50, 60, -30, -80, -78, -75, -70]
        # Create a figure and axis
        #self.fig, self.ax = plt.subplots()
        # Initialize a line plot showing the action potential over time
        self.line, = self.ax.plot(self.time, self.potential, "green") #self.draw_color
        self.ax.plot(self.time, self.potential)
        self.ax.axis('off')
        #self.fig.set_facecolor('#54545a')

    #Function to update the plot for each frame of the animation
    def anim_update(self,num):
        """Update Function for the animation running along the differen potential steps

        Args:
            num (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.line.set_data(self.time[:num], self.potential[:num])
        return self.line,

    def start_animation_timer(self):
        """Starts the animation timer for the AP animation!
        """
        self.anim = animation.FuncAnimation(self.fig, self.anim_update, frames=len(self.time), blit=True)
        # Show the plot on the QWidget
        # Create a QTimer
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(lambda: self.anim.event_source.start())
        self.canvas.draw_idle()

    def stop_animation(self):
        self.anim.event_source.stop()
