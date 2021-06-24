import tkinter.ttk as ttk
import tkinter as tk
from PIL import ImageTk ,Image
from tkinter import filedialog
import pandas as pd


class BackendElements():

    def __init__(self):

        # Initialize the GUI component to check states
        self.cam_button = None
        self.camera = None
        self.reload = None
        self.ex = None
        self.cancel = None
        self.canvas = None


    def backend_notes(self, bm, note, window, cam):

            '''settings of the backend communication'''

            window.option_add("*foreground","black")
            

            ### box1
            self.row1 = ttk.Frame(master=note.frames[1], style="grey.TFrame")
            self.row2 = ttk.Frame(master=note.frames[1], style="grey.TFrame")
            self.row3 = ttk.Frame(master=note.frames[1], style="grey.TFrame")
            self.row4 = ttk.Frame(master=note.frames[1], style="grey.TFrame")
            self.row5 = ttk.Frame(master=note.frames[1], style="grey.TFrame")

            self.experiment_data = ttk.Frame(master= note.frames[0])
            self.experiment_data.grid(row = 2, column = 1, columnspan = 3)
            self.load_data_button = ttk.Frame(master = note.frames[0])
            self.load_data_button.grid(column = 1, row = 1, columnspan = 2)

            #load metadata button

            self.experiment_button = ttk.Button(self.load_data_button,
                                                text = "Load Experiment Data",
                                                width = 20,
                                                command = self.load_experiment_data,
                                                style = "AccentButton")

            self.experiment_button.grid(column = 1, row = 1, sticky = "w", pady = 10)
            
            # row 1
            self.path_label = ttk.LabelFrame(self.row1, text="Control File Template")
            self.path_label.pack(side='left', padx=10)

            self.path_string = ttk.Label(self.path_label, text= bm.control_path, width=100)
            self.path_string.pack(padx=10)

            # row 2
            self.browse_button = ttk.Button(self.row2, text="Search Control File Template ",
                                           command=bm.set_controlpath, width=30)
            self.browse_button.pack(side=tk.LEFT, padx=5)
            # TODO path update required: reload notebook ?

            self.generate_control_template = ttk.Button(self.row2, text="Generate Control File Template ",
                                                       command=bm.set_controlpath, width=30)
            self.generate_control_template.pack(side=tk.LEFT, padx=5)
            self.view_commands = ttk.Button(self.row2, text="View Commands",
                                           command=bm.set_controlpath, widt=30)
            self.view_commands.pack(side=tk.LEFT, padx=5)

            # row 3
            self.batch_path_label = ttk.LabelFrame(self.row3, text="Batch Path")
            self.batch_path_label.pack(side='left')
            self.batch_path_string = ttk.Label(self.batch_path_label, text= bm.batch_path, width=100)
            self.batch_path_string.pack()

            # row 4
            self.browse_batch_button = ttk.Button(self.row4, text="Set Batch Path", command=lambda: self.set_path(bm),
                                                 width=30)
            self.browse_batch_button.pack(side='left', padx=5)
            self.generate_batch_control = ttk.Button(self.row4, text="Generate Control File",
                                                    command=bm.create_ascii_file_from_template,
                                                    width=30)
            self.generate_batch_control.pack(side='left', padx=5)

            self.row1.pack(pady=10)
            self.row2.pack(pady=5)
            self.row5.pack(pady=20)  # just an empty row
            self.row3.pack(pady=10)
            self.row4.pack(pady=5)

            # when the run button was pressend .. it should change from red to green

            ########## Communication Log
            # should check if the backend instance has already an active communication running
            # an active communication is defined as an opened e9Batch.out file

            ## out would be nice to see what the rquest-response-chart looks like


            #@ TODO make these Labels scrollable
            self.requested_commands = ttk.LabelFrame(master=note.frames[2], text="Control File")
            self.requested_commands_details = ttk.Label(self.requested_commands,
                                                        text=bm.control_file_content,
                                                        width=50)  # self.bm.get_control_file_content())
            self.requested_commands_details.grid(pady=10, padx=5)
            self.requested_commands.grid(column = 1, row = 2, rowspan = 3, padx=50)

            self.patch_master_response = ttk.LabelFrame(master=note.frames[2], text="Response File")
            self.patch_master_response_details = ttk.Label(self.patch_master_response,
                                                           text=bm.response_file_content, width=50)
            self.patch_master_response_details.grid(pady=10, padx=5)
            self.patch_master_response.grid(column = 1, row = 1)

            self.command_text_box = tk.Text(master=note.frames[2],height=15,fg="white", bg = "#392d52", width = 40)
            self.command_text_box.grid(column = 2, row = 1, rowspan = 3, padx = 10, pady = 10)

            self.command_text_box.configure(state = "disabled")


            self.button_frame = ttk.Frame(note.frames[2])
            self.button_frame.grid(column = 2, row = 4, pady = 10)
            # @TODO the output windows are always one step behind. why ? fix update method anyway !
            self.read_and_send=ttk.Button(self.button_frame, 
                                         text="Send Control Command",
                                         command= lambda: self.get_commands_from_textinput(bm),
                                         style = "AccentButton")
            
            self.read_and_send.configure(state = "disabled")

            self.enable_editing = ttk.Checkbutton(self.button_frame,
                                            text = "Enable Protocol Editing",
                                            style = "Switch",
                                            onvalue = 1,
                                            offvalue = 0,
                                            command = self.disable_state
                                            )

            self.enable_editing.grid(column = 1, row = 1, padx = 5)
            self.read_and_send.grid(column = 2, row = 1, padx = 5)  # A tk.DrawingArea.
            
            ############################################################################
            #make a camera interface
            ############################################################################

            self.cam = cam # maker camera object instance variable

            # draw the canvas frame for the camera 
            self.camframe = ttk.Frame(master = note.frames[3])
            self.camframe.grid()

            # TODO check state of the canvas for saving procedures?

            #initialize the cam automatically
            self.init_camera(bm)

    def load_experiment_data(self):
        """ Loads the location of the metadata 
        Author MZ"""
        metadata_files = filedialog.askopenfilename(master=self.load_data_button,
                                                    title = "Select Metadata",
                                                    filetypes = (("CSV Files","*.csv"),))
        
        metadata = pd.read_csv(metadata_files)
        self.write_experiment_data(metadata)

    def write_experiment_data(self, csv_data):
        """ Writes the LabelFrames hard coded maybe change into loops, dictionary or ?
        Author MZ """

        labelframe_content = ["Compound","Solutions","Cells","Experimental Protocol","Archiving","Staff"]
        labelframe_list = []

        for i,t in enumerate(labelframe_content):
            if (i)%2 == 0:
                label_data = ttk.LabelFrame(self.experiment_data, text = t, width = 530, height = 300)
                labelframe_list.append(label_data)
                label_data.grid(column = 1, row = int((i/2+1)), padx = 5)
                label_data.grid_propagate(0)
            else:
                label_data = ttk.LabelFrame(self.experiment_data, text = t, width = 670, height = 300)
                labelframe_list.append(label_data)
                label_data.grid(column = 2, row = int((int(i)/2+1)), padx = 5)
                label_data.grid_propagate(0)

        #entries and labels for all the data
        sample_code_label = ttk.Label(labelframe_list[0], text = "Sample Code")
        sample_code_entry = ttk.Entry(labelframe_list[0])
        sample_code_label.grid(column = 1, row = 1, pady = 4, padx = 5)
        sample_code_entry.grid(column = 1, row = 2, pady = 4, padx = 5)

        lot_label = ttk.Label(labelframe_list[0], text = "Lot #")
        lot_entry = ttk.Entry(labelframe_list[0])
        lot_label.grid(column = 2, row = 1, pady = 4, padx = 5)
        lot_entry.grid(column = 2, row = 2, pady = 4, padx = 5)

        salt_label = ttk.Label(labelframe_list[0], text = "Salt code")
        salt_entry = ttk.Combobox(labelframe_list[0])
        salt_label.grid(column = 3, row = 1, padx = 5, pady = 5)
        salt_entry.grid(column = 3, row = 2, padx = 5, pady = 5)

        sample_id_label = ttk.Label(labelframe_list[0], text = "Sample ID")
        sample_id_label_entry = ttk.Entry(labelframe_list[0])
        sample_id_label.grid(column = 1, row = 3, padx = 5, pady =5)
        sample_id_label_entry.grid(column = 1, row = 4, padx = 5, pady = 5)

        mw_label = ttk.Label(labelframe_list[0], text = "MW [Da]")
        mw_label_entry = ttk.Entry(labelframe_list[0])
        mw_label.grid(column = 2, row = 3, padx = 5, pady = 5)
        mw_label_entry.grid(column = 2, row = 4, padx = 5, pady = 5)

        weight_label = ttk.Label(labelframe_list[0], text = "Weight [mg]")
        weight_label_entry = ttk.Entry(labelframe_list[0])
        weight_label.grid(column = 1, row = 5, padx = 5, pady = 5)
        weight_label_entry.grid(column = 1, row = 6, padx = 5, pady = 5)

        solvent_label = ttk.Label(labelframe_list[0], text = "Solvent")
        solvent_label_entry = ttk.Entry(labelframe_list[0])
        solvent_label.grid(column = 2, row = 5, padx = 5, pady = 5)
        solvent_label_entry.grid(column = 2, row = 6, padx = 5, pady = 5)
        
        volume_label = ttk.Label(labelframe_list[0], text = "Volume [µl]")
        volume_label_entry = ttk.Entry(labelframe_list[0])
        volume_label.grid(column = 3, row = 5, padx = 5, pady = 5)
        volume_label_entry.grid(column = 3, row = 6, padx = 5, pady = 5)

        stocks_label = ttk.Label(labelframe_list[0], text = "Stocks [mM]")
        stocks_label_entry = ttk.Entry(labelframe_list[0])
        stocks_label.grid(column = 1, row = 7, padx = 5, pady = 5)
        stocks_label_entry.grid(column = 1, row = 8, padx = 5, pady = 5)

        conc_label = ttk.Label(labelframe_list[0], text = "Concentration [µM]")
        conc_label_entry = ttk.Entry(labelframe_list[0])
        conc_label.grid(column = 2, row = 7, padx = 5, pady = 5)
        conc_label_entry.grid(column = 2, row = 8, padx = 5, pady = 5)

        solution_2_label = ttk.Label(labelframe_list[1], text = "EC type")
        solution_2_combo = ttk.Combobox(labelframe_list[1], width = 40)
        solution_2_label.grid(column = 1, row = 1, padx = 5, pady = 5, columnspan = 4)
        solution_2_combo.grid(column = 1, row = 2, columnspan = 4, padx = 5, pady = 5)

        ic_2_label = ttk.Label(labelframe_list[1], text = "IC type")
        ic_2_combo = ttk.Combobox(labelframe_list[1], width = 40)
        ic_2_label.grid(column = 1, row = 3, padx = 5, pady = 5, columnspan = 4)
        ic_2_combo.grid(column = 1, row = 4, columnspan = 4, padx = 5, pady = 5)

        ec_lot_label = ttk.Label(labelframe_list[1], text = "EC lot #")
        ec_lot_entry = ttk.Entry(labelframe_list[1])
        ec_lot_label.grid(column = 2, row = 5, padx = 5, pady = 5)
        ec_lot_entry.grid(column = 2, row = 6, padx = 5, pady = 5)

        ic_lot_label = ttk.Label(labelframe_list[1], text = "IC lot #")
        ic_lot_entry = ttk.Entry(labelframe_list[1])
        ic_lot_label.grid(column = 3, row = 5, padx = 5, pady = 5)
        ic_lot_entry.grid(column = 3, row = 6, padx = 5, pady = 5)

        temp_lot_label = ttk.Label(labelframe_list[1], text = "T [°C]")
        temp_lot_entry = ttk.Entry(labelframe_list[1])
        temp_lot_label.grid(column = 1, row = 7, padx = 5, pady = 5)
        temp_lot_entry.grid(column = 1, row = 8, padx = 5, pady = 5)

        f_lot_label = ttk.Label(labelframe_list[1], text = "F [mL/min]")
        f_lot_entry = ttk.Entry(labelframe_list[1])
        f_lot_label.grid(column = 2, row = 7, padx = 5, pady = 5)
        f_lot_entry.grid(column = 2, row = 8, padx = 5, pady = 5)

        i_lot_label = ttk.Label(labelframe_list[1], text = "I [nm]")
        i_lot_entry = ttk.Entry(labelframe_list[1])
        i_lot_label.grid(column = 3, row = 7, padx = 5, pady = 5)
        i_lot_entry.grid(column = 3, row = 8, padx = 5, pady = 5)

        e_lot_label = ttk.Label(labelframe_list[1], text = "e")
        e_lot_entry = ttk.Entry(labelframe_list[1])
        e_lot_label.grid(column = 4, row = 7, padx = 5, pady = 5)
        e_lot_entry.grid(column = 4, row = 8, padx = 5, pady = 5)

        cells_2_label = ttk.Label(labelframe_list[2], text = "License ID")
        cells_2_combo = ttk.Combobox(labelframe_list[2])
        cells_2_label.grid(column = 1, row = 1, padx = 5, pady = 5, columnspan = 4)
        cells_2_combo.grid(column = 1, row = 2, columnspan = 4, padx = 5, pady = 5)

        cell_line_2_label = ttk.Label(labelframe_list[2], text = "Cell Line")
        cell_line_2_combo = ttk.Entry(labelframe_list[2])
        cell_line_2_label.grid(column = 1, row = 3, padx = 5, pady = 5)
        cell_line_2_combo.grid(column = 1, row = 4, padx = 5, pady = 5)

        passage_label = ttk.Label(labelframe_list[2], text = "# Passage")
        passage_combo = ttk.Entry(labelframe_list[2])
        passage_label.grid(column = 4, row = 3, padx = 5, pady = 5)
        passage_combo.grid(column = 4, row = 4, padx = 5, pady = 5)

    def get_commands_from_textinput(self,bm):
        print("get commands")
        self.res = self.command_text_box.get("1.0","end")
        print(self.res)
        bm.send_text_input(self.res)
        self.update_page_2()
        self.update_page_2()
        return self.res

    def update_page_2(self):
        self.requested_commands_details.update_idletasks()
        self.patch_master_response.update_idletasks()

    def disable_state(self):
        print(self.enable_editing.state())
        if "selected" in self.enable_editing.state():
            print("yes")
            self.command_text_box.configure(state = "normal")
            self.command_text_box.configure(bg = "#121010")
            self.read_and_send.configure(state = "normal")
        else:
            self.command_text_box.configure(state = "disabled")
            self.command_text_box.configure(bg = "#392d52")
            self.read_and_send.configure(state = "disabled")

    def set_path(self, bm):
        # set the batch path 
        path = bm.set_batch_path()
        self.batch_path_string.configure(text = path)

     
    def init_camera(self,bm, reload = None):
        # Initialize the Camera if camera not initaliazed yet
        #load buton if camera is initialize
        if self.camera:
            self.draw_cam_buttons(2,bm)
            return print("Camera already in use:")

        if reload:
            self.exceptfunction() # write an except if its not working
            self.reload = ttk.Button(self.camframe, text = "Reinitialize Camera", command = lambda: self.init_camera(bm), style = "AccentButton")
            self.reload.grid(column = 3, row = 3, pady = 10, padx = 20, ipadx = 10, ipady = 10)
            return False

        self.camera = self.cam.init_camera(self.camframe)
        self.init_camera(bm,True) # reload if failed and load a button 
    

    def draw_cam_buttons(self,init, bm):
        """ draw the cam button, necessary to start the cam and the api to the cam drivers
        Author MZ """ 
        
        col_number = range(3 + init)
        # Draw the buttons for the camera Start, Stop Save
        if self.reload:
            self.reload.destroy()

        self.camera_label = ttk.LabelFrame(self.camframe, text = "Camera Frame")
        self.camera_label.grid(column = 1, row = 2, sticky = "w", pady = 10)

        button_frame = ttk.Frame(self.camframe)
        button_frame.grid(row = 1, column = 1, sticky = "w")
        cam_button = ttk.Button(button_frame, text = "Live Stream", command = self.camera_connection)
        cam_button.grid(column = col_number[0], row = 1,padx = 2, sticky = "w", pady = 5)

        stop_button = ttk.Button(button_frame, text = "Stop Stream", command = self.cancel_job)
        stop_button.grid(column = col_number[1], row =1 , padx = 2, sticky = "w", pady = 5)

        save_button = ttk.Button(button_frame, text = "Save Image", command = lambda: self.cam.save_fig(bm))
        save_button.grid(column = col_number[2], row = 1, padx = 2, sticky = "w", pady = 5)

    def camera_connection(self):
        # Start the video grabbing
        # Author MZ
        img = self.cam.grab_video()
        self.draw_canvas(img)

    def exceptfunction(self):
        # Except when camera is not found or connected
        # Author MZ
        if self.ex:
            self.ex.destroy()
        self.ex = tk.Label(master = self.camframe, text="Please connect the Camera!", bg = "#602470")
        self.ex.grid(column = 1, row = 2)

    def draw_canvas(self, img):
        """ draw the canvas image for the camera""" 
            
        self.canvas = tk.Canvas(self.camera_label, width = 400, height = 400)
        self.canvas.grid(column = 1, row = 1, sticky = "nswe")
        imgs = Image.fromarray(img)
        image = imgs.resize((400,400), Image.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(image=image)
        self.canvas.create_image(20,20, anchor=tk.NW, image=imgtk)
        self.canvas.image = imgtk
        self.cancel = self.canvas.after(333, self.camera_connection)

    def cancel_job(self):
        if self.cancel:
            self.canvas.after_cancel(self.cancel)
            self.cancel = None
        else:
            print("Please connect to the camera")

    

     



