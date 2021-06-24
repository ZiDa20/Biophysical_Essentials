import tkinter as tk
import tkinter.ttk as ttk
import matplotlib as mpl
from tkinter_camera import *
import os
from PIL import ImageTk, Image

plt.style.use('dark_background')
mpl.use('TkAgg')
plt.rcParams['axes.facecolor']='#333333'
plt.rcParams['figure.facecolor'] ='#333333'
mpl.rc('axes',edgecolor='black')

class FrontPage():

    def __init__(self, appearance, self_button_state = 0):

        self.welcome_window = tk.Tk()
        self.welcome_window.title("Welcome to ETools")
        # specify style
        self.s = ttk.Style(self.welcome_window)
        self.appearance = appearance
        self.style_button = self_button_state
        self.themes_call()
        self.s.theme_use(self.appearance)
        self.s.configure('welcome.TButton', font=("Times", 22))

        self.mode_selection()
        

        #start the app
        
    def themes_call(self):
        if self.appearance == "azure":
            self.welcome_window.tk.call("source", os.getcwd() + "/../Azure_theme/azure.tcl")
        else:
            self.welcome_window.tk.call("source",os.getcwd() +"/../Azure_theme/azure-dark.tcl")

    def mode_selection(self):
        
        logo_frame = ttk.Frame(self.welcome_window)
        logo_frame.grid(column = 1, row = 1)
        logo = Image.open("../Logo/random_trial.png")
        logo = logo.resize((200,200),Image.ANTIALIAS)

        logo = ImageTk.PhotoImage(logo)
        image_frame = tk.Label(logo_frame,image = logo)
        image_frame.image = logo
        welcome_label = ttk.Label(logo_frame, text="Etools Main Menu")

        button_icr = ttk.Button(logo_frame,
                                      text="Intra Cellular Recordings",
                                      command=self.open_icr_menu,
                                      width = 30,
                                      )

        button_ecr = ttk.Button(logo_frame,
                                      text="Extra Cellular Recordings",
                                      command=self.open_ecr_menu,
                                      width = 30
                                      )

        button_doc = ttk.Button(logo_frame,
                                text = "Documentation",
                                width = 30)

        self.switch_mode = tk.BooleanVar()
        self.switch_mode.set(self.style_button)

        style_toggle = ttk.Checkbutton(logo_frame,
                                  text = "Switch to Dark Mode",
                                  var = self.switch_mode,
                                  style = "Switch",
                                  command = self.switch_theme)

        style_toggle.grid(row = 5, column = 1, pady = 10)
        welcome_label.configure(font=("Times",30))
        image_frame.grid(row=1,column = 1)

        #welcome_label.grid(row=2,column=1, pady = 5)
        button_icr.grid(row=2,column=1, ipady=40, pady = 5, sticky = "w")
        button_ecr.grid(row=3, column =1, ipady=40, pady = 5, sticky = "w")
        button_doc.grid(row=4, column = 1, pady = 5,ipady = 40, sticky = "w")

    def open_icr_menu(self):
        from frontend import GuiEtools  # needed here to "avoid" circular dependencies - at least to simulate this for python
        icr_handler = GuiEtools(self.welcome_window, appearance = self.appearance)
        return icr_handler

    def open_ecr_menu(self):
        from frontend import GuiEtools
        ecr_handler = GuiEtools(self.welcome_window, appearance = self.appearance)
        return ecr_handler

    def switch_theme(self):
        print(self.switch_mode.get())
        if self.switch_mode.get() == False:
            self.appearance = "azure"
            self.welcome_window.destroy()
            FrontPage(self.appearance,0)
        else:
            self.appearance = "azure-dark"
            self.welcome_window.destroy()
            FrontPage(self.appearance, 1)

if __name__ == "__main__":
    FrontPage("azure").welcome_window.mainloop()
