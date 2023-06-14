import matplotlib
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation

class LoadingAnimation(QDialog):

    def __init__(self, message, frontend_style, parent = None):
        """_summary_
        """
        super().__init__(parent)
        self.message: str = message
        self.setup_ui()
        self.frontend_style = frontend_style
        self.call_frontend_style()
        self.time = None
        self.potential = None
        self.setWindowTitle("Processing ...")
        
        # Set the fixed size of the dialog
        self.setFixedSize(800, 500)
        
    def call_frontend_style(self):
        if self.frontend_style.default_mode == 0:
            self.frontend_style.set_mpl_style_dark()
            self.draw_color = "white"
            self.ax_color = "white"
        else:
            self.frontend_style.set_mpl_style_white()
            self.draw_color = "black"
            self.ax_color = "black"
        
        self.frontend_style.set_pop_up_dialog_style_sheet(self)

    def setup_ui(self):
        self.progress_bar = QProgressBar()
        #self.progress_bar.setFixedWidth(250)
        self.progress_bar.setAlignment(Qt.AlignLeft)
        self.status_bar = QLabel()
        self.animated_canvas = QWidget()
        self.grid_animated = QVBoxLayout(self)
        self.label_description = QLabel(self.message)
        self.font = QFont()
        self.font.setPointSize(25)
        self.label_description.setFont(self.font)
        self.label_description.setAlignment(Qt.AlignCenter)

        self.grid_animated.addWidget(self.label_description)
        self.fig = Figure(figsize=(4,4))
        self.canvas = FigureCanvas(self.fig)
        #self.canvas.setParent(self.animated_canvas)
        self.grid_animated.addWidget(self.canvas)
        self.grid_animated.addWidget(self.progress_bar)
        self.grid_animated.addWidget(self.status_bar)
        
    def make_widget(self):
        self.create_ap_line_out()
        self.start_animation_timer()
        self.show_dialog()
    
    def stop_and_close_animation(self):
        self.stop_animation()
        self.accept()

    def show_dialog(self):
        self.show()
        QCoreApplication.processEvents()

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
        self.line, = self.ax.plot(self.time, self.potential, self.draw_color)
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

    def progress_bar_update_analysis(self, data):
        """ This function will update the progress bar in the analysis tab
        :param data:

        """
        self.progress_bar.setValue(data[0])
        #self.statusbar.showMessage("Analyzing: " + str(data[1]) + "%")
        self.status_bar.setText(f"Current Progress: {str(data[0])}%")

    def stop_animation(self):
        self.anim.event_source.stop()
        self.timer.stop()
