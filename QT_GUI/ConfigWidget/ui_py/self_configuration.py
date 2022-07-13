import sys
import os
sys.path.append(os.path.dirname(os.getcwd()) + "/QT_GUI/ConfigWidget/CustomWidgets")
sys.path.append(os.path.dirname(os.getcwd()) + "/QT_GUI/ConfigWidget/ui_py")
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from PIL import ImageQt ,Image
from backend_manager import *
import os.path
import logging
from dragable_label import *
from tkinter_camera import *
from time import sleep
import pandas as pd
import pyqtgraph as pg
pg.setConfigOption('foreground', '#ff8117')
from dvg_pyqtgraph_threadsafe import PlotCurve
from self_config_notebook_widget import *
import traceback, sys
from functools import partial


class Config_Widget(QWidget,Ui_Config_Widget):
    
    def __init__(self, online, progress_bar, status_bar, parent = None,):
        """Initialize the configuration widget
        args:
            online type(bool): if the program is online or not
            progress_bar type(QProgressBar): progress bar for the progress of the experiment
            status_bar type(QStatusBar): status bar for the status of the experiment
            parent type(QWidget): parent widget
        returns:
            None
        """
        super(Config_Widget,self).__init__(parent) # initialize the parent class
        # initialize self_config_notebook_widget
        self.setupUi(self) # setup the ui file 
        self.CameraDock.setAllowedAreas(Qt.TopDockWidgetArea)
        self.CameraWindow.addDockWidget(Qt.TopDockWidgetArea, self.CameraDock)
        # added the Progress Bar to the self-configuration
        self.set_buttons_beginning()
        
        #select the batch_path
        self.batch_path = None
        self.backend_manager = BackendManager() # initialize the backend manager
        self.online_analysis = online # load the backend manager
        
        # add the progresbar and status bar
        self.progressBar = progress_bar   
        self.statusBar = status_bar

        # Experiment Section
        ## pathes for the pgf files
        self.pgf_file = None
        self.pro_file = None
        self.onl_file = None
        self.data_file_ending = 1
        self.general_commands_list = ["GetEpcParam-1 Rseries", "GetEpcParam-1 Cfast", "GetEpcParam-1 Rcomp","GetEpcParam-1 Cslow","Setup","Seal","Whole-cell"]
        self.config_list_changes = ["Whole Cell", "Current Clamp"]
        self.check_connection.setText("Warning: \n \nPlease select the PGF, Analysis and Protocol File and set the Batch communication Path!")
        self.experiment_dictionary = {} # create and experiment dictionary with Metadata
        self.submission_count = 2 # each submitte command will increase counts 

        ## setup pyqtgraph for experiment visualization
        self.pyqt_graph = pg.PlotWidget(height = 100) # insert a plot widget
        self.pyqt_graph.setBackground("#232629")

        # Camera Section
        
        self.image_stack = [] # stack of images
        self.image_list = []
        self._image_count = 0

        #darkmode
        self.default_mode = 1
        
        # check if session is implemeted
        self.check_session = None

        # Initialize the connections  
        self.logger_setup()      
        self.initialize_camera()
        self.connections_clicked_experiment()
        self.connections_clicked_camera()
        self.connection_clicked_threading()
        
        self.set_solutions()

    def connection_clicked_threading(self):
        """ connect button to the threading"""
        self.start_experiment_button.clicked.connect(self.make_threading) # spawns the thread
        self.stop_experiment_button.clicked.connect(self.terminate_sequence) # terminate sequence to patchmater

    def connections_clicked_camera(self):
        """ connect the buttons to the camera """        
        self.button_start_camera.clicked.connect(self.start_camera_timer) # intialize 
        self.button_stop_camera.clicked.connect(self.stop_camera)
        self.button_take_snapshot.clicked.connect(self.show_snapshot)

    def connections_clicked_experiment(self):
        """ connect the buttons to the experiment """
        self.Load_meta_data_experiment_12.clicked.connect(self.meta_open_directory) # retrieve the metadata from txt file
        self.button_batch_1.clicked.connect(self.set_batch_path) # establish batch_path
        self.establish_connection_button.clicked.connect(self.open_batch_path) # checks if the connection is owrking
        self.button_pgf_set.clicked.connect(self.set_pgf_file) # sets pgf file
        self.button_protocol_set.clicked.connect(self.set_protocol_file) # sets protocol file
        self.button_onl_analysis_set.clicked.connect(self.set_online_file) # sets online analysis file
        self.button_submit_command.clicked.connect(self.get_commands_from_textinput) # submit command for testing
        self.button_clear_window.clicked.connect(self.end_communication_control) # clear the window
        self.pushButton_10.clicked.connect(self.clear_list) # is cleaning ListViews
        self.switch_to_testing.clicked.connect(self.switch_testing) # switches to the tesing mode

    def logger_setup(self):
        # logger added --> ToDO: should be used for developers as well as for users should be disriminated
        print("initialized the logger")
        self.logger= logging.getLogger() 
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('../Logs/patchmaster_communication.log')
        formatter  = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.debug('A debug message')
    
    def set_solutions(self):
        """ set solutions that you can use for the experiment"""
        extracellular_solutions = ["ECS Standard","ECS Standard new","Sodium ECS", "Potassium ECS","Calcium ECS","aCSF","NMDG Solution", "low-calcium ECS"]
        intracellular_solutions = ["Pipette XX","Pipette XXneu"]

        for i in extracellular_solutions:
            self.extracellular_sol_com_1.addItem(i)
        
        for i in intracellular_solutions:
            self.Intracellular_sol_com_1.addItem(i)
   
    
    def set_buttons_beginning(self):
        """ set the buttons to the beginning state"""
        self.transfer_to_online_analysis_button.setEnabled(False)
        

    def meta_open_directory(self):
        '''opens a filedialog where a user can select a desired directory. Once the directory has been choosen,
        it's data will be loaded immediately into the databse'''
        # open the directory
        dir_path = QFileDialog.getOpenFileName()
        dir_path = str(dir_path[0]).replace("/","\\")
        # save the path in the manager class
        return dir_path

    def set_pgf_file(self):
        """set the pgf file that is used for the patchmaster"""
        logging.info("Setted PGF File")
        self.pgf_file = self.meta_open_directory()
    
        self.pg_file_set.setText(self.pgf_file)

    def set_protocol_file(self):
        """set the .pro file that is used for the patchmaster"""
        logging.info("Setted Protocol File")
        self.pro_file = self.meta_open_directory()
        self.protocol_file_set.setText(self.pro_file)

    def set_online_file(self):
        """set the online_analysis_file that is used for the patchmaster"""
        logging.info("Setted online analysis file")
        self.onl_file = self.meta_open_directory()
        self.online_analysis_file_set.setText(self.onl_file)

    def set_dat_file_name(self, name):
        """set the dat file name that is used for the patchmaster
        args:
            name type(string): name of the dat file
        returns:
            None
        """
        name = name + "_" + str(self.data_file_ending) + ".dat"
        print(name)
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + f"OpenFile new {name}" + "\n")
        sleep(0.5) 
        self.increment_count() # increment the count for the patch 
        self.data_file_ending += 1 # increment the data file ending

    def set_batch_path(self):
        """ set the path for the batch files located"""
        self.batch_path = self.backend_manager.set_batch_path()
        self.Batch1.setText(self.batch_path)

    def get_file_path(self):
        """get the file were the current datafile is located
        ToDO add this to a database --> for report of the overall labbook"""
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + f"GetParameters DataFile" +"\n")
        sleep(0.5)
        self.increment_count()
        file_name = self.backend_manager.update_response_file_content()
        file_path = file_name.split('"')[1]

        self.data_file_ending += 1 # update after transfer to online_analysis so that a new file can be used
        self.set_dat_file_name(self.experiment_type_desc.text())
        return file_path

    def save_to_database(self):
        # Add here the function to retrieve the database
        # After click the data is written into dictionary --> ToDO: might be transfered into the database by DZ 
        print("save the data to the database")
        self.data_file = self.experiment_type_desc.text()

        # Can be saved for the whole experiment
        # We should add an experiment name
        self.extracellular_and_intra = {"extracellular_solution": self.extracellular_sol_com_1.currentText(),
                                        "intracellular_solution": self.Intracellular_sol_com_1.currentText(),
                                        "Preparation Date": self.ent_date_prep.text(),
                                        "pH extracellular": self.S2_3.text(),
                                        "ph intracellular": self.ent_ph_int_set.text()}
        
        # ToDO: experiment metadata should be saved after each file please change MZ
        self.experiment_metadata = {"Cell Type:": self.cell_type_desc.text(),
                                    "# Cells": self.min_number_cells.text(),
                                    "# Patched Cells": self.patched_cells.text()}

        
    def open_batch_path(self):
        """ choose the path were the batch communication file should
        be located
        --> checks for the exisitence of the file
        --> check control file button should indicate if file is already 
        there
         """
        
        if self.batch_path: # if the path is already set

            try:
                file_existence = self.backend_manager.check_input_file_existence()
                self.backend_manager.create_ascii_file_from_template()
                self.submit_patchmaster_files()
                self.set_dat_file_name(self.experiment_type_desc.text())
                #self.self_configuration_notebook.setCurrentIndex(1)
                self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "SendOnlineAnalysis notebook" +"\n")
                sleep(1)
                self.increment_count()
                self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "ConnectionIdentify" +"\n")
                self.increment_count()
                sleep(1)
                connection = self.backend_manager.read_connection_response() # here we should check the response of the connection

            except Exception as e: # if the file does not exist
                self.logger.error(f"Patchmaster not connected properly: {e}")
                self.check_connection.setText("Patchmaster not connected properly, please check the path and the Batch files")
                self.statusBar.showMessage("Patchmaster not connected properly, please check the path and the Batch files")
 
            if connection: # if the connection is established
                self.logger.info("Connection established")
                self.check_connection.setText("Connected: \n \nBatch Communication successfully connect \n \nToDo: \n \n Change to the Batch Communication Tab \n \n Patchmaster Message: \n \n" + connection)
                self.statusBar.showMessage("Connection to Patchmaster successfully established")
 
            else: # if the connection is not established
                self.logger.warning("Connection to Patchmaster failed")
                self.check_connection.setText("Connection to Patchmaster failed")
                self.statusBar.showMessage("Connection to Patchmaster failed")
    
              
        else:   # if the path is not set
            self.logger.info("No batch path set")
            self.Batch1.setText("please select a Path for the Patch File")

        self.show_analysis_window() # show the analysis window

    def switch_testing(self):
        """Switch to testing or to the plot visualization triggered by the button
        Its for potential problems between the connection of the heka patchmaster and the programm"""

        current_notebook_index = self.visualization_stacked.currentIndex() # get the current index of the notebook
        if current_notebook_index == 1: # if the current notebook is the plot notebook
            self.visualization_stacked.setCurrentIndex(0)
            self.switch_to_testing.setText("Switch to Plot")
        else: # if the current notebook is the testing notebook
            self.visualization_stacked.setCurrentIndex(1)
            self.switch_to_testing.setText("Switch to Testing")
            
    def initialize_camera(self):
        """ Basler camera initalizing  
        ToDO: Error handling"""

        self.logger.info("Camera will be initialized") # log the event
        self.camera = BayerCamera() # initialize the camera
        #initialize the camera 
        camera_status = self.camera.init_camera() # initialize the camera
        self.scence_trial = QGraphicsScene(self) # generate a graphics scence in which the image can be putted
        if camera_status is None: # initialization of the camera and error response if not correctly initialized
            self.scence_trial.addText("Camera is not connected please check the connection in the settings app")
            self.logger.warning("Camera was not found please check the connection")
            self.Camera_Live_Feed.setScene(self.scence_trial) # set the scene to the live feed
            self.button_start_camera.setEnabled(False)
            self.button_stop_camera.setEnabled(False)
            self.button_take_snapshot.setEnabled(False)

        else:
            self.logger.info("Camera is connected!") # log the event
            self.scence_trial.addText("Please start capturing!")
            self.Camera_Live_Feed.setScene(self.scence_trial)

    def start_camera_timer(self):
        """ added the asnychronous Qtimer for the Camera initalizion"""
        try:
            self.start_cam = QTimer() # create a timer
            self.start_cam.timeout.connect(self.start_camera) # connect the timer to the start camera function
            self.start_cam.start(33) # start the timer with a time interval of 222 ms
            self.logger.info("Qthread for Camera caption is running")
        except Exception as e:
            self.logger.error(f"Here is the Error description of the camera running task: {e}")


    def start_camera(self):
        """ grab the current picture one by one with 50 FPS """
        camera_image = self.camera.grab_video() # grab video retrieved np.array image
        self._image_count += 1 # increment the image count
        imgs = Image.fromarray(camera_image) # conversion
        image = imgs.resize((451,300), Image.ANTIALIAS) # resizing to be of appropriate size for the window
        imgqt = ImageQt.ImageQt(image) # convert to qt image
        self.camera_image_recording = QPixmap.fromImage(imgqt) # convert to qt pixmap
        self.scence_trial.clear()   # clear the scene
        self.scence_trial.addPixmap(self.camera_image_recording)
        
        if self._image_count % 33 == 0:
            self.draw_video(self.camera_image_recording)

    def stop_camera(self):
        """ Stopping the Qthread for the Camera """
        self.start_cam.stop() # here the camera Qtimer is stopped
        self._image_count = 0
        self.camera_stopped_transfer_video()
        #self.logger("Camera Thread is stopped")

    def show_snapshot(self):
        """ does transfer the current snapshot to the galery view """
        image_list = self.check_list_lenght(self.image_stack) # self.image_stack is der stack der images generiert
        image_list.insert(0,self.camera_image_recording) # neues image wird an stelle 1 gepusht
        self.snapshot_scence = QGraphicsScene(self) # generate a graphics scence in which the image can be putted
        self.Taken_Snapshot.setScene(self.snapshot_scence) # set the scene to the taken snapshot
         # set the scene to the online analysis
        self.snapshot_scence.addPixmap(self.camera_image_recording) # add the image to the scene
        self.online_analysis.draw_scene(self.camera_image_recording)
        self.draw_snapshots_on_galery(image_list) # draw into the galery


    def draw_video(self, imgs):
        """ draw the video in the live feed 
        args:
            imgs type: numpy array  of the current image
        """
        try:
            self.image_list.append(imgs)
        except Exception as e:
            print(e)
        
    
    def camera_stopped_transfer_video(self):
        """ transfer the video to the galery view """
        print("transfer video")
        self.online_analysis.video_mat = self.image_list
        print(len(self.online_analysis.video_mat))
        self.image_list = []

    def check_list_lenght(self, image_liste):
        """Here we check the length of the Image Stack to push them out after 5 Images

        Args:
            image_liste (list): List of captured numpy arrays

        Returns:
            list: Image List of size 5
        """        
        try:
            if len(image_liste) > 4: # if stack overcrowded
                image_liste.pop() # remove the last image
                self.logger.info("Stacked is crowded pushing last image out")
                return image_liste
            else:
                return image_liste
        except Exception as e:
            print(repr(f"This is the Error: {e}"))  # print the error

    def draw_snapshots_on_galery(self, image_list):
        # function to draw the taken snapshot into the image galery
        for i in reversed(range(self.camera_horizontal.count())): 
            self.camera_horizontal.itemAt(i).widget().setParent(None)
        if len(self.image_stack) > 0: #looping through the image stack
            for i,t in enumerate(image_list):

                label = QPushButton() # we set a label in the layout which should then be filled with the pixmap
                label.setStyleSheet("height: 150px;background-color: rgba(0,0,0,0); border:1px solid #fff5cc;")
                label.clicked.connect(partial(self.online_analysis.draw_scene,t)) # connect the label to the draw scene function
                label.setIcon(QIcon(t)) # we set the pixmap to the label
                label.setIconSize(QSize(200,280)) # we set the size of the pixmap
                label.setFixedWidth(200)
                
                self.camera_horizontal.addWidget(label, alignment=Qt.AlignCenter) # add to the layout 

    def get_commands_from_textinput(self):
        """ retrieves the command send to the patchmaster and the response from the Batch.out file """
        print("get commands")
        self.res = self.sub_command1.toPlainText() 
        self.logger.debug(f'Batch communication input: {self.res}')
        self.sub_command1.clear() # clear the text input
        self.get_commands_from_textinput_2(self.res)
        

    def get_commands_from_textinput_2(self, res):
        """" retrieves the command send to the patchmaster and the response from the Batch.out file 
        args:
            res (str): string of the command send to the patchmaster
        returns:
            str: string of the response from the Batch.out file
        """
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + res + "\n")
        self.logger.info("This command was send to the patchmaster: ""+"+f'{self.submission_count}' + "\n" + res + "\n")
        self.submission_count += 1
        if self.check_session:
            print("still checking commands")
        else:
            self.check_session = QTimer() # timer added for regular checking 
            self.check_session.timeout.connect(self.update_page)
            self.check_session.start(1000)
        #return self.res

    def update_page(self):
        """ asynchronouse updating of the textArea with the control file and the response file
        Connected to the Qtimter """
        response_file = self.backend_manager.update_response_file_content() # response file update
        input_file = self.backend_manager.update_control_file_content() # control file update
        self.receive_command1.clear()# clearing of the last commands entered
        self.response_command_1.clear() # clearing of the response
        self.receive_command1.insertPlainText(input_file)
        self.response_command_1.insertPlainText(response_file)

    def end_communication_control(self):
        """ stop the batch communication and clear all fields """
        print("communication end")
        if self.check_session:
            self.check_session.stop() # stops the timer
            self.check_session = None
            self.receive_command1.clear()
            self.response_command_1.clear()
            self.sub_command1.clear()

    def show_analysis_window(self):
        """ show the analysis window """
        # Get Input from the Sequences and the Protocols
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "ListSequences\n") # get the potential Series that can be started
    
        self.logger.info("send this comment: " "+"+f'{self.submission_count}' + "\n" + "ListSequences\n")
        sleep(0.2) # sleep is inserted because of laggy writing to the response file from the patchmaster
        sequences = self.backend_manager.update_response_file_content()
        self.increment_count()
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "ListProtocols\n") # get the protocols that can be started
        self.logger.info("send this comment: " "+"+f'{self.submission_count}' + "\n" + "ListProtocols\n")
        sleep(0.2)
        protocol_responses = self.backend_manager.update_response_file_content() # get the protocol responses 
        self.increment_count() # always increment the batch communication count 

        # Plotting
        self.tscurve_1 = PlotCurve(
            linked_curve=self.pyqt_graph.plot(pen=pg.mkPen('r')),
        ) # use this package to make drawing from another thread Threadsafe
        self.pyqt_window.addWidget(self.pyqt_graph) # add the graph to the window

        # Preprocessing
        series = self.preprocess_series_protocols(sequences) # get the listed series from batch.out response
        protocols = self.preprocess_series_protocols(protocol_responses) # get the listed protocols from batch.out response

        #Make List Labels
        self.make_sequence_labels(series, self.SeriesWidget) # enter items of sequences into drag and dropbable listview
        self.make_sequence_labels(protocols, self.protocol_widget) # enter items of protcols into drag and dropable listview
        self.make_general_commands() # add general commands to the general command listview
        self.make_config_commands() # add config commands to the config command listview
        self.visualization_stacked.setCurrentIndex(1) # set the index to the testing Area

    def preprocess_series_protocols(self, sequences_reponses):
        """ preprocess the sequences and protocols from the batch.out response
        args:
            sequences_reponses (str): string of the sequences and protocols from the batch.out response
        returns:
            patch_sequences (list): list of the sequences from the batch.out response
        """
        patch_sequences = sequences_reponses[31: ].split(",")
        patch_sequences = [i.replace('"', "") for i in patch_sequences]
        patch_sequences = [i.replace("\n", "")for i in patch_sequences]
        return patch_sequences
         
    def make_sequence_labels(self, list_of_sequences,widget):
        """ make the labels for the sequences and protocols
        args:
            list_of_sequences (list): list of the sequences from the batch.out response
            widget (QWidget): widget to add the labels to
        returns:
            None
        """
        for i in list_of_sequences:
            item = QStandardItem(i)
            widget.model().appendRow(item)

    def make_general_commands(self):
        """ make the general commands for the general command listview """
        for i in self.general_commands_list:
            item = QStandardItem(i)
            self.general_commands_labels.model().appendRow(item)

    def make_config_commands(self):
        """make commands into the listview for configuration of whole cell and current clamp
        ' We should avoid duplicates here so me must check for this and disallow dropping to this lists"""
        for i in self.config_list_changes:
            item = QStandardItem(i)
            self.SeriesWidget_2.model().appendRow(item)

    def submit_patchmaster_files(self):
        """ Submission of the loaded pgf, prot and onl file to the patchmaster and setting them"""
        self.logger.info("Configuration Files setted up:....")
        # set the files
        for file, command in zip([self.pgf_file, self.pro_file, self.onl_file],["OpenPgfFile","OpenProtFile","OpenOnlineFile"]):
            if file:
                self.backend_manager.send_text_input("+"+f'{self.submission_count}\n' + command + f" {file}\n") # send the file lcoation and name to the patchmaster
                sleep(0.5)
                self.submission_count += 1
            else:
                logging.info("not all configuration files set:")

    def make_threading(self):
        """ make the threading for the communication with the patchmaster """
        try: 
            self.threadpool = QThreadPool() # create the threadpool
            self.worker = Worker(self.start_experiment_patch) # create the worker
            self.worker.signals.finished.connect(self.thread_complete) # connect the worker to the thread_complete function
            self.worker.signals.progress.connect(self.online_analysis.draw_live_plot)# connect the worker to the draw_live_plot function
            self.threadpool.start(self.worker) # start the worker
        except Exception as e: 
            print(e)

    def thread_complete(self):
        print("THREAD COMPLETE!")    

    def stop_threading(self):
        # Here we need to find a way to stop the threading if an error occur !
        self.threadpool.stop(self.worker)

    def start_experiment_patch(self, progress_callback):
        """ start the experiment with the patchmaster 
        args:
            progress_callback (function): function to call when the progress is updated
        returns:
            None
        """
        # this should be exposed to threading!
        view_list = self.listWidget.model()
        self.sequence_experiment_dictionary = {} # all derived online analyiss data will be stored here in a "Series":Data fashion
        self.increment_count()
        final_notebook_dataframe = pd.DataFrame() # initialize an empty dataframe which can be appended to
        # goes through the list, when the list is done the transfer to online analysis button will turn green and transfer is possible
        for index in range(view_list.rowCount()):

            # start the progress bar
            max_value = (len(range(view_list.rowCount()))+1)
            value = (index+1) * (100/max_value)
            self.progressBar.setValue(value)
            self.progressBar.setFormat(f"{value}/100")

            # retrieve the series or protocol
            item = view_list.item(index).text() # get the name of the stacked protocols/series/programs
            
            # send it via batch communication
            self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""GetParameters Param-2,Param-3,Param-4,Param-12\n") # always check the parameters after each protocol
            #ToDO Define Cancel Options like Filters
            sleep(0.3) # sleep for allowing program write and read

            #this should update the parameters for each sweep and run
            params_response = self.backend_manager.get_parameters() 
            self.increment_count()
            sleep(0.5)

            # here we set the text
            self.set_params(params_response)
            
            # Check which kind of parameter is queried
            if self.SeriesWidget.model().findItems(item):
                """ check if item is in series list"""
                logging.info(f"Series {item} will be executed")
                self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "ExecuteSequence " + f'"{item}"' +"\n")
                self.increment_count()
                self.trial_setup(final_notebook_dataframe, item, progress_callback)

            elif "GetEpc" in item:
                #check if item is a paramter check
                logging.info(f"Parameter Command {item} will be executed")
                self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + f'"{item}"' +"\n")
                print("GetParameters if necessary")
            
            elif self.protocol_widget.model().findItems(item):
                #Check if item is a protcol
                logging.info(f"Protocol {item} will be executed")
                self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "ExecuteProtocol " + f'"{item}"' +"\n")
                self.increment_count()
                analyzed = self.trial_setup(final_notebook_dataframe, item, progress_callback)

            elif self.general_commands_labels.model().findItems(item):
                #check if item is a general command
                logging.info(f"General Command {item} will be executed")
                self.basic_configuration_protcols(item)

            else:
                #check if item is a general command
                logging.info(f"Config Command change to: {item} will be executed")
                self.change_mode_protocols(item)
                sleep(0.3)

        # turn the button green if sequence finished succesfully
        self.progressBar.setValue(100)
        self.transfer_to_online_analysis_button.setEnabled(True)

    def set_params(self, params_response):
        """Retrieve the Parameter value and add to the entry boxes

        Args:
            params_response (list): List of Paramater 
        """        
        self.rseries_qc.setText(params_response[3])
        self.cslow_qc.setText(params_response[1])
        self.cfast_qc.setText(params_response[0])
        self.cfast_qc_2.setText(params_response[2])

    def increment_count(self):
        #increment count to renew submission code for the patchmaster
        self.submission_count += 1

    def trial_setup(self, notebook, item, progress_callback):
        """ setup the trial for the experiment
        args:
            notebook (pd.DataFrame): dataframe to append to
            item (str): name of the series/protocol
            progress_callback (function): function to call when the progress is updated
        returns:
            analyzed (bool): True if the protocol was analyzed, False if not
        """
        sleep(0.2) # sleeping to avoid overflue by commands added to the batch communication
        item = item 
        final_notebook_dataframe = notebook # maybe deep copy
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "Query\n") # Query to get the state of the amplifier
        self.increment_count()

        query_status = self.backend_manager.get_query_status() # get the status of the query
        query_status = query_status.replace(" ", "")# post processing
        print(f"this is the query status: {query_status}")

        if "Query_Idle" in query_status:
            # Check for different states
            try: 
                dataframe = self.backend_manager.return_dataframe_from_notebook()
                final_notebook_dataframe = final_notebook_dataframe.append(dataframe)
                final_notebook = self.get_final_notebook(final_notebook_dataframe)
                self.sequence_experiment_dictionary[item] = final_notebook

            except Exception as e:
                print(repr(e))
                final_notebook = self.get_final_notebook(final_notebook_dataframe)
                self.sequence_experiment_dictionary[item] = final_notebook
                return True
    
        elif any(text in query_status for text in ["Query_Acquiring","Query_Executing"]):
            print("yes executing")
            #Check if the query is still acquiring
            try:
                dataframe = self.backend_manager.return_dataframe_from_notebook()
                final_notebook_dataframe = final_notebook_dataframe.append(dataframe)

                # usually this should write also in the online analysis still not functional!
                progress_callback.emit(([float(i) for i in final_notebook_dataframe.iloc[1:,:][4].values],[float(i) for i in final_notebook_dataframe.iloc[1:,:][7].values]))
                self.tscurve_1.setData([float(i) for i in final_notebook_dataframe.iloc[1:,:][4].values],[float(i) for i in final_notebook_dataframe.iloc[1:,:][7].values])
                self.tscurve_1.update()

                # here drawing should be provided to the online analysis class
                self.trial_setup(final_notebook_dataframe,item, progress_callback)

            except Exception as e:
                print(repr(e))
                self.trial_setup(final_notebook_dataframe,item, progress_callback)
        
        else:
            print("Connection Lost")
            return None
        
    def get_final_notebook(self, notebook):
        """ gets the final notebook and returns it
        
        args:
            notebook (pandas.DataFrame): notebook dataframe
            
        returns:
            notebook (pandas.DataFrame): notebook dataframe"""
        columns = notebook.iloc[0].tolist()
        columns.pop(0)
        columns = columns + ["NAN"] # add a column for the time stamp
        columns = [str(i).replace('"',"") for i in columns]
        final_notebook = notebook[1:]
        final_notebook.columns = columns
        final_notebook = final_notebook.iloc[:,4:]
        final_notebook = final_notebook.drop("NAN", axis = 1)
        return True

    def basic_configuration_protcols(self, item):
        """Executes the basic configuration protocols
        
        args:
            item (str): item to be executed
            
        returns:
            None"""

        function_dictionary = {"Setup": self.execute_setup, "Seal": self.execute_seal, "Whole-cell": self.execute_whole_cell}
        func = function_dictionary.get(item,lambda :'Invalid')
        func()

    def change_mode_protocols(self, item):
        """Executes the change mode protocols
        
        args:
            item (str): item to be executed
        returns:
            None
        """

        function_dictionary = {"Whole Cell": self.whole_cell,"Current Clamp": self.current_clamp, "Holding Potential": self.holding, "C-slow compensation": self.compensate}
        func = function_dictionary.get(item, lambda: "Invalid")
        func()

    def whole_cell(self):
        """Executes the whole cell protocol
        
        args:
            None
        returns:
            None
        """
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""Set E Mode 3; Whole Cell\n")
        self.increment_count()

    def holding(self):
        """Sets the holding potential mode"""
        #TODO: add the holding potential mode
        print("Add here the holding potential")

    def compensate(self):
        """Sets the C-slow compensation mode
        args:
            None
        returns:
            None
        """
        print("Add here the compensation function")

    def current_clamp(self):
        """Sets the current clamp mode
        args:
            None
        returns:
            None
        """
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""Set E Mode 4; C-Clamp\n")
        self.increment_count()

    def execute_setup(self):
        """Executes the setup protocol
        args:
            None
        returns:
            None
        """
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""ExecuteProtocol SETUP\n")
        self.increment_count()
    
    def execute_seal(self):
        """Executes the seal protocol
        args:
            None
        returns:
            None
        """
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""ExecuteProtocol SEAL\n")
        self.increment_count()
    

    def execute_whole_cell(self):
        """Executes the whole cell protocol
        args:
            None
        returns:
            None
        """
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""ExecuteProtocol WHOLE-CELL\n")
        self.increment_count()


    def terminate_sequence(self):
        """Terminates the sequence
        args:
            None
        returns:
            None
        """
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "Terminate\n") # Query to get the state of the amplifier
        self.increment_count()

            
    def clear_list(self):
        """Clears the list of experiments
        args:
            None
        returns:
            None
        """
        self.listWidget.model().clear()
        
    def set_darkmode(self, default_mode):
        """Sets the dark mode"""
        self.default_mode = default_mode
   
    def get_darkmode(self):
        "returns the darkmode state"
        print(f"this is the current mode: {self.default_mode}")
        return self.default_mode

    def setting_appearance(self):
        """Sets the appearance of the application
        args:
            None
        returns:
            None
        """
        default_mode = self.get_darkmode()
        if default_mode == 0:
            print("light_mode")
            self.pyqt_graph.setBackground("#f5f5f5")

        else:
            print("dark_mode")
            self.pyqt_graph.setBackground("#232629")


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()  # QtCore.Slot
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    new_worker = Signal()
    progress = Signal(tuple)