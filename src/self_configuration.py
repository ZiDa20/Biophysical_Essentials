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
from dropable_list_view import ListView
from plotting_pyqt import PlotClass
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
pg.setConfigOption('foreground', '#ff8117')
from dvg_pyqtgraph_threadsafe import PlotCurve
from self_config_notebook_widget import *


class Config_Widget(QWidget,Ui_Config_Widget):
    """ promotion of the self configuration widget"""
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)

        # initialize self_config_notebook_widget
        self.setupUi(self)
        self.set_buttons_beginning()
    


        self.batch_path = None
        self.backend_manager = BackendManager()
        self.pgf_file = None
        self.pro_file = None
        self.onl_file = None
        self.general_commands_list = ["GetEpcParam-1 Rseries", "GetEpcParam-1 Cfast", "GetEpcParam-1 Rcomp","GetEpcParam-1 Cslow","Setup","Seal","Whole-cell"]
        self.submission_count = 2
        self.image_stacke = []
        self.default_mode = 1
        self.pyqt_graph = pg.PlotWidget(height = 100) # insert a plot widget
        self.pyqt_graph.setBackground("#232629")
        self.setupUi(self)
        self.check_session = None
        self.logger=logging.getLogger() 
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('../Logs/configuration.log')
        print(file_handler)
        formatter  = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.debug('A debug message')

        self.Load_meta_data_experiment_12.clicked.connect(self.meta_open_directory) # initialize meta data sheet opening boehringer special

        #connect to the camera control
        self.pushButton.clicked.connect(self.initialize_camera) # initalize the camera 
        self.button_start_camera.clicked.connect(self.start_camera_timer) # intialize 
        self.button_stop_camera.clicked.connect(self.stop_camera)
        self.button_take_snapshot.clicked.connect(self.show_snapshot)

        #connect to the function for the batch communication
        self.button_batch_1.clicked.connect(self.open_batch_path)
        self.button_batch_2.clicked.connect(self.show_analysis_window)
        self.button_pgf_set.clicked.connect(self.set_pgf_file)
        self.button_protocol_set.clicked.connect(self.set_protocol_file)
        self.button_onl_analysis_set.clicked.connect(self.set_online_file)
        self.button_submit_command.clicked.connect(self.get_commands_from_textinput)
        self.button_clear_window.clicked.connect(self.end_communication_control)
        # initialize the camera module

        #threading
        self.pushButton_3.clicked.connect(self.make_threading)
        self.pushButton_10.clicked.connect(self.clear_list)
        self.pushButton_4.clicked.connect(self.stop_threading)


        
    def set_buttons_beginning(self):
        """ set the button state of a view buttons inactivate at the beginning"""
        self.button_batch_2.setEnabled(False)
        self.add_pixmap_for_green.setStyleSheet("color: red")

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

    def open_batch_path(self):
        """ choose the path were the batch communication file should
        be located
        --> checks for the exisitence of the file
        --> check control file button should indicate if file is already 
        there
         """
        batch_path = self.backend_manager.set_batch_path()
        if batch_path:
            self.Batch1.setText(batch_path)
            self.batch_path = batch_path
            file_existence = self.backend_manager.check_input_file_existence()
            self.backend_manager.create_ascii_file_from_template()
            self.button_batch_2.setStyleSheet("background-color: green")
            self.button_batch_2.setEnabled(True)
            self.submit_patchmaster_files()
            self.Notebook_2.setCurrentIndex(1)
            self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "SendOnlineAnalysis notebook" +"\n")
            self.increment_count()
                           
        else:
            self.Batch1.setText("please select a Path for the Patch File")

    def initialize_camera(self):
        """ Basler camera initalizing  
        ToDO: Error handling"""

        print("stuff worked")
        self.camera = BayerCamera()
        #initialize the camera 
        camera_status = self.camera.init_camera()
        self.scence_trial = QGraphicsScene(self) # generate a graphics scence in which the image can be putted
        if camera_status is None: # initialization of the camera and error response if not correctly initialized
            self.scence_trial.addText("is not working")
            self.Camera_Live_Feed.setScene(self.scence_trial)
            self.button_start_camera.setEnabled(False)
            self.button_stop_camera.setEnabled(False)
            self.button_take_snapshot.setEnabled(False)

        else:
            print("Camera is connected")
            self.scence_trial.addText("Please start the Camera via the Start Camera Button")
            self.Camera_Live_Feed.setScene(self.scence_trial)

    def start_camera_timer(self):
        """ added the asnychronous Qtimer for the Camera initalizion"""
        self.start_cam = QTimer() # camera timer 
        self.start_cam.timeout.connect(self.start_camera)   # connected to camera methond
        self.start_cam.start(222)  # (333,self.start_camera)

    def start_camera(self):
        """ grab the current picture one by one with 50 FPS """
        camera_image = self.camera.grab_video() # grab video retrieved np.array image
        imgs = Image.fromarray(camera_image) # conversion
        image = imgs.resize((561,451), Image.ANTIALIAS) # resizing to be of appropriate size for the window
        imgqt = ImageQt.ImageQt(image) # convert to qt image
        self.trial_figure = QPixmap.fromImage(imgqt)
        self.scence_trial.clear()
        self.scence_trial.addPixmap(self.trial_figure)
        print(camera_image)

    def stop_camera(self):
        """ stop the camera timer """
        print("yeah I m here for the camera")
        self.start_cam.stop() # here the camera Qtimer is stopped

    def show_snapshot(self):
        """ does transfer the current snapshot to the galery view """

        self.check_list_lenght(self.image_stacke) # self.image_stacke is der stack der images generiert
        self.image_stacke.insert(0,self.trial_figure) # neues image wird an stelle 1 gepusht
        self.snapshot_scence = QGraphicsScene(self)
        self.Taken_Snapshot.setScene(self.snapshot_scence)
        self.snapshot_scence.addPixmap(self.trial_figure)
        self.draw_snapshots_on_galery() # draw into the galery

    def check_list_lenght(self, image_liste):
        """Here we check the lenght of the  to avoid overcrowding in the image galery
        its set to 5 images"""
        try:
            if len(image_liste) > 4:
                image_liste.pop()
                print("Expected List Length reached")
        except Exception as e:
            print(repr(f"This is the Error: {e}"))


    def draw_snapshots_on_galery(self):
        # function to draw the taken snapshot into the image galery
        for i in reversed(range(self.horizontalLayout.count())): 
            self.horizontalLayout.itemAt(i).widget().setParent(None)
        if len(self.image_stacke) > 0: #looping through the image stack
            for i,t in enumerate(self.image_stacke):
                label = QLabel()
                label.setPixmap(t)
                self.horizontalLayout.addWidget(label) # add to the layout 


    def get_commands_from_textinput(self):
        """ retrieves the command send to the patchmaster and the response from the Batch.out file """
        print("get commands")
        self.res = self.sub_command1.toPlainText()
        self.logger.debug(f'Batch communication input: {self.res}')
        self.sub_command1.clear()
        
        print(self.res)
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + self.res + "\n")
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
        """add Docstring"""
        # Get Input from the Sequences and the Protocols
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "ListSequences\n") # get the potential Series that can be started
        sleep(0.2) # sleep is inserted because of laggy writing to the response file from the patchmaster
        sequences = self.backend_manager.update_response_file_content()
        self.increment_count()
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "ListProtocols\n") # get the protocols that can be started
        sleep(0.2)
        protocol_responses = self.backend_manager.update_response_file_content() # get the protocol responses 
        self.increment_count() # always increment the batch communication count 

        # Plotting
        
        self.tscurve_1 = PlotCurve(
            linked_curve=self.pyqt_graph.plot(pen=pg.mkPen('r')),
        ) # use this package to make drawing from another thread Threadsafe
     # setting of the background put to global
        self.pyqt_window.addWidget(self.pyqt_graph)
        #self.plot_qt(self.pyqt_graph.plotWidget)

        # Preprocessing
        series = self.preprocess_series_protocols(sequences) # get the listed series from batch.out response
        protocols = self.preprocess_series_protocols(protocol_responses) # get the listed protocols from batch.out response
        self.style_list_view()

        #Make List Labels
        self.make_sequence_labels(series, self.SeriesWidget) # enter items of sequences into drag and dropbable listview
        self.make_sequence_labels(protocols, self.protocol_widget) # enter items of protcols into drag and dropable listview
        self.make_general_commands() # add general commands to the general command listview
        self.stackedWidget.setCurrentIndex(1) # set the index to the testing Area

    def preprocess_series_protocols(self, sequences_reponses):
        """get the list of protocols,get rid of the submission code"""
        patch_sequences = sequences_reponses[31: ].split(",")
        patch_sequences = [i.replace('"', "") for i in patch_sequences]
        patch_sequences = [i.replace("\n", "")for i in patch_sequences]
        return patch_sequences
        
    def style_list_view(self):
        """ styling of the ListWidget make it blue to popup more"""
        self.listWidget.setStyleSheet(f"border: 2px; background: #31363b; color :#ff8117 ")
        self.SeriesWidget.setStyleSheet("background: #31363b;")
        self.general_commands_labels.setStyleSheet("background: #31363b")
        self.protocol_widget.setStyleSheet("background: #31363b")

    def make_sequence_labels(self, list_of_sequences,widget):
        """ same as protocols"""
        for i in list_of_sequences:
            item = QStandardItem(i)
            widget.model().appendRow(item)

    def make_general_commands(self):
        #insert items into general command list
        for i in self.general_commands_list:
            item = QStandardItem(i)
            self.general_commands_labels.model().appendRow(item)

    def submit_patchmaster_files(self):
        """ Submission of the loaded pgf, prot and onl file to the patchmaster and setting them"""
        logging.info("Configuration Files setted up:....")
        for file, command in zip([self.pgf_file, self.pro_file, self.onl_file],["OpenPgfFile","OpenProtFile","OpenOnlineFile"]):
            if file:
                self.backend_manager.send_text_input("+"+f'{self.submission_count}\n' + command + f" {file}\n") # send the file lcoation and name to the patchmaster
                sleep(0.5)
                self.submission_count += 1
            else:
                logging.info("not all configuration files set:")

    def make_threading(self):
        # generate a threadpool inherted from the runnable class and connect it to the workerclass
        self.threadpool = QThreadPool()
        self.worker = Worker(self.start_experiment_patch)
        self.threadpool.start(self.worker)

    def stop_threading(self):
        # Here we need to find a way to stop the threading if an error occur !
        self.threadpool.stop(self.worker)

    def start_experiment_patch(self):
        """ get the ListView entries and send them off via the backend manager"""
        # this should be exposed to threading!
        view_list = self.listWidget.model()
        self.sequence_experiment_dictionary = {} # all derived online analyiss data will be stored here in a "Series":Data fashion
        self.increment_count()
        final_notebook_dataframe = pd.DataFrame() # initialize an empty dataframe which can be appended to
        
        for index in range(view_list.rowCount()):
            item = view_list.item(index).text() # get the name of the stacked protocols/series/programs
            self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""GetParameters Param-2,Param-3,Param-4,Param-12\n") # always check the parameters after each protocol
            #ToDO Define Cancel Options like Filters
            sleep(0.2)
            params_response = self.backend_manager.get_parameters() # return the paramters and write them into the entry boxes
            self.increment_count()
            self.rseries_qc.setText(params_response[3])
            self.cslow_qc.setText(params_response[1])
            self.cfast_qc.setText(params_response[0])
            self.cfast_qc_2.setText(params_response[2])

            if self.SeriesWidget.model().findItems(item):
                """ check if item is in series list"""
                logging.info(f"Series {item} will be executed")
                self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "ExecuteSequence " + f'"{item}"' +"\n")
                self.increment_count()
                self.trial_setup(final_notebook_dataframe, item)

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
                analyzed = self.trial_setup(final_notebook_dataframe, item)

            else:
                #check if item is a general command
                logging.info(f"General Command {item} will be executed")
                self.basic_configuration_protcols(item)


    def increment_count(self):
        #increment count to renew submission code for the patchmaster
        self.submission_count += 1

    def trial_setup(self, notebook, item):
        """gets the data and draws it into the fast analysis window
        ToDO:"""
        sleep(0.2)
        item = item 
        final_notebook_dataframe = notebook
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "Query\n") # Query to get the state of the amplifier
        self.increment_count()

        query_status = self.backend_manager.get_query_status()
        query_status = query_status.replace(" ", "")
        print(f"this is the query status: {query_status}")

        if "Query_Idle" in query_status:
            # Check for different states
            try: 
                dataframe = self.backend_manager.return_dataframe_from_notebook()
                final_notebook_dataframe = final_notebook_dataframe.append(dataframe)
                final_notebook = self.get_final_notebook(final_notebook_dataframe)
                self.sequence_experiment_dictionary[item] = final_notebook
            except:
                final_notebook = self.get_final_notebook(final_notebook_dataframe)
                self.sequence_experiment_dictionary[item] = final_notebook
                return True
    
        elif ("Query_Acquiring" or "Query_Executing") in query_status:
            #Check if the query is still acquiring
            try:
                dataframe = self.backend_manager.return_dataframe_from_notebook()
                final_notebook_dataframe = final_notebook_dataframe.append(dataframe)
                print(final_notebook_dataframe)
                print(final_notebook_dataframe.iloc[1:,:][4].values)
                self.tscurve_1.setData([float(i) for i in final_notebook_dataframe.iloc[1:,:][4].values],[float(i) for i in final_notebook_dataframe.iloc[1:,:][7].values])
                self.tscurve_1.update()
                self.trial_setup(final_notebook_dataframe,item)
            except Exception as e:
                print(repr(e))
                self.trial_setup(final_notebook_dataframe,item)
        
        else:
            print("Connection Lost")
            return None
        

    def get_final_notebook(self, notebook):
        """ Dataframe has multiple commas therefore columsn will be shifted to adjust for this"""
        columns = notebook.iloc[0].tolist()
        columns.pop(0)
        columns = columns + ["NAN"]
        columns = [str(i).replace('"',"") for i in columns]
        final_notebook = notebook[1:]
        final_notebook.columns = columns
        final_notebook = final_notebook.iloc[:,4:]
        final_notebook = final_notebook.drop("NAN", axis = 1)
        
        print(final_notebook)
        return True

    def basic_configuration_protcols(self, item):
        print("yes i entered this file")
        function_dictionary = {"Setup": self.execute_setup, "Seal": self.execute_seal, "Whole-cell": self.execute_whole_cell}
        func = function_dictionary.get(item,lambda :'Invalid')
        func()

    def execute_setup(self):
        # setup protocol execturio command
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""ExecuteProtocol SETUP\n")
        self.increment_count()
    
    def execute_seal(self):
        # seal protocol exectuion command
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""ExecuteProtocol SEAL\n")
        self.increment_count()
        print()

    def execute_whole_cell(self):
        #whole_cell exection command 
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""ExecuteProtocol WHOLE-CELL\n")
        self.increment_count()
        print(9)
        
    def clear_list(self):
        # connect to the button 
        self.listWidget.model().clear()
        
    def set_darkmode(self, default_mode):
        self.default_mode = default_mode
   
    def get_darkmode(self):
        "returns the darkmode state"
        print(f"this is the current mode: {self.default_mode}")
        return self.default_mode

    def setting_appearance(self):
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

    @Slot()  # QtCore.Slot
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)