import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AnimatedAP:
    def __init__(self):

        matplotlib.rcParams['toolbar'] = 'None'
        # Define the time points at which the action potential will be sampled
        self.time = [0, 1, 2, 3, 4, 5,6,7,8,9,10]

        # Define the values of the action potential at each time point
        self.potential = [-60, -59, -53, -50,-50, 60, -30, -80, -78, -75, -70]

        # Create a figure and axis
        self.fig, self.ax = plt.subplots()

        # Initialize a line plot showing the action potential over time
        self.line, = self.ax.plot(self.time, self.potential, 'maroon')
        self.ax.plot(self.time, self.potential, 'lightgrey')
        self.ax.axis('off')
        self.fig.set_facecolor('#54545a')

       
    #Function to update the plot for each frame of the animation
    def anim_update(self,num):
        self.line.set_data(self.time[:num], self.potential[:num])
        return self.line,

    def show_dialog(self):
          plt.show()