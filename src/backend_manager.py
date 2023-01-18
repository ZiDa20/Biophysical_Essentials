import os.path
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import pandas as pd
from time import sleep
import numpy as np


class BackendManager:
    '''Manager class to handle all the backend communication'''

    def __init__(self):
        self._control_path = "/"   # path where the template for the controlfile is expected
        self._batch_path= "/media/archiv3/Projekt_Daten/HEKA/patch_master_data_path" # path where patch master will expect the batch-control file
        self.controlfile = False    # per default this is false, if the file has been generated, it will become true
        # @TODO what happens if the string becomes to big ?
        self._control_file_content = "Select a control file first"
        self._response_file_content = "No active communication"


    @property
    def control_path(self):
        return self._control_path

    @control_path.setter
    def control_path(self,val):
        self._control_path=val

    # setter required
    def set_controlpath(self):
        self._control_path = self.select_path()

    def select_path(self):
        selected_path = QFileDialog.getExistingDirectory()
        return selected_path

    @property
    def batch_path(self):
        return self._batch_path

    @batch_path.setter
    def batch_path(self,val):
        self.batch_path=val

    def set_batch_path(self):
        self._batch_path= self.select_path()
        return self._batch_path

    @property
    def control_file_content(self):
        return self._control_file_content

    @control_file_content.setter
    def control_file_content(self,val):
        self._control_file_content=val

    @property
    def response_file_content(self):
        return self._response_file_content

    @response_file_content.setter
    def response_file_content(self,val):
        self._response_file_content = val


    def controlpath_valid(self):
        if not self.control_path:
            return False
        else:
            return True

    # a function to read the content of the E9Batch.In file
    def update_control_file_content(self):
        if self._batch_path:
            self.cf_content=open(self.batch_path+'/E9Batch.In', "r")
            self.cmd = self.cf_content.read()
            self.cf_content.close()
            print("The control file content was updated")
            self._control_file_content=self.cmd
            # @TODO should think about a delay
            self.update_response_file_content()
            return(self.cmd)
        else:
            return('No batch control file found ! \n Please set the batch path first')

    # a function to read the content of the E9Batch.OUT file
    def update_response_file_content(self):
        try:
            self.rf_content = open(self.batch_path + '/E9Batch.OUT', "r")
            self.rspns= self.rf_content.read()
            self.rf_content.close()
            self._response_file_content=self.rspns
            return(self.rspns)
        except FileNotFoundError:
            return('There was no .OUT file found. Is the communication active ?')

    def get_query_status(self):
        """Get the query status of the File"""
        sleep(1)
        try:
            with open(self.batch_path + '/E9Batch.OUT', "r") as file_object:
                query_status = file_object.readlines()[1]
                file_object.close()
                return query_status
        except Exception as e:
            print(e)


    def get_epc_param(self):
        """Get the query status of the File"""
        sleep(1)
        try:
            with open(self.batch_path + '/E9Batch.OUT', "r") as file_object:
                epc_param = file_object.readlines()[1]
                epc_param = epc_param.split(" ")[1]
                file_object.close()
                return epc_param
        except Exception as e:
            print(e)


    def get_parameters(self):
        """get Patch Clamp Paramters for viewing Parameters"""
        sleep(0.5)
        response = self.get_query_status()
        response = response.split(" ")[1:]
        return response


    def return_dataframe_from_notebook(self):
        """Get the DataFrame from the notebook analysis"""
        data_frame_notebook = pd.read_csv(self.batch_path + '/E9Batch.OUT', skiprows = 2, header = None)
        data_frame_notebook = data_frame_notebook.loc[:, data_frame_notebook.dtypes == float]
        #data_frame_notebook = data_frame_notebook.iloc[:,4:]
        return data_frame_notebook
        
        
    def create_ascii_file_from_template(self):
        # create a new e9Patch file
        if not self.batch_path:
            return False
        else:
            try:
                self.batch_file = open(self.batch_path+'/E9Batch.In', "w")
                self.batch_file.write("+1\n")
                self.batch_file.write("GetTime \n")
                self.batch_file.close()
                self.update_control_file_content()
                #copyfile(self.batch_path + '/E9Batch.In', self.batch_path + '/E9BatchIn.txt')
                print("Batch control file generated succesfully")
                return True
            except Exception as error:
                print(repr(error))
                # TODO catch error of an already existing file
                # TODO catch error of no x-rights at the desired location
                return False
        # fill e9patch file with content from the template
        # TODO check template path to be not empty
        # TODO copy content of the template into the ascii file - only use one identifier initially
        #print(self.batch_path)
        #self.batch_file.open(self.batch_path+'/E9Patch.In', "a")
        #self.batch_file.close()


    def send_text_input(self,input_string=None):
        print("send text-input function\n")
        if not input_string:
            input_string="+2 \n GetTime"
            print(input_string)
            print(type(input_string))
        else:
            print("strange string\n")
            
        try:
                self.c_f= open(self.batch_path + '/E9Batch.In', "r+")
                self.old_commands = self.c_f.read()
                self.c_f.seek(0,0)
                self.new_commands = input_string+ "\n" + self.old_commands
                self.c_f.write(self.new_commands)
                self.update_control_file_content()
                self.c_f.close()

        except Exception as error:
                print(repr(error))


    def get_response_file_content(self):
        # asynchron read seems to be dependent from the used os
        #toDO; shouldnt we use context manager for this? 
        self.response_file_content = open(self.batch_path + '/E9BatchOut.txt', "r")

    def check_input_file_existence(self):
        return os.path.exists(self.batch_path + '/E9Batch.In')

    def get_file_path(self, increment):
        self.send_text_input()

    def read_connection_response(self):
        with open(self.batch_path + '/E9Batch.Out', "r") as file_object:
                epc_param = file_object.read()
                print(epc_param)
                return epc_param
        
    #def transfer_data_to_offline(self, name):
    #    #should transfer the .dat file if closed or analysis finished