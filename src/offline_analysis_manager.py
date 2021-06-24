import tkinter.ttk as ttk
import tkinter as tk
import raw_analysis as ra
from tkinter import filedialog
import os
import heka_reader
from online_analysis_manager import *

import data_db


class OfflineManager():

    def __init__(self):
        self.meta_path = None
        self.dat_files = None

        # nodelist for the treeview
        self.directory_content_list = [['','','']]

        #list of filterelements and their parameters
        self.filter_list = []

        # list of series specific analysis functions and their coursor bounds
        self.series_specific_analysis_list=[]

        # database object
        self.database = data_db.DataDB()



    # Database functions
    def init_database(self):
        self.database.create_analysis_database()
        self.database.create_database_tables()

    def write_analysis_series_types_to_database(self,series_type_list):
        self.database.write_analysis_series_types_to_database(series_type_list)

        # initial filter settings
        self.database.write_filter_into_database("CSlow", -10, +10)
        self.database.write_filter_into_database("RSeries", -12, +20)

    def write_series_type_specific_experiment_and_sweep_information(self,data_list,series_name):
        '''fill database from series type specific treeview list, no duplicated insertation'''
        self.database.fill_database_from_treeview_list(data_list,series_name)

    def write_analysis_function_to_database(self,function_selection,series_name):
        self.database.write_analysis_function_to_database(function_selection,series_name)

    def write_coursor_bounds_to_database(self,left_coursor, right_coursor, series_name):
        self.database.write_coursor_bounds_to_database(left_coursor, right_coursor, series_name)

    def read_trace_data_and_write_to_database(self,series_name):
        self.database.read_trace_data_and_write_to_database(series_name,self.dat_files)

    def calculate_single_series_results_and_write_to_database(self,series_name):
        self.database.calculate_single_series_results_and_write_to_database(series_name)

    def read_series_type_specific_analysis_functions_from_database(self,series_name):
        '''function that will return a list of strings with analysis function names'''
        return self.database.read_series_type_specific_analysis_functions_from_database(series_name)



    def ask_file(self, frame):
        frame.option_add("*foreground","black")
        metadata_files = filedialog.askopenfilename(master=frame)
        return metadata_files#
    
    def ask_directory(self, frame, treeview):
        frame.option_add("*foreground","black")
        directory_path = filedialog.askdirectory(master=frame, initialdir=os.getcwd())
        data_list = self.package_list(directory_path)

        # DZ: to be able to reload, the list needs to be reset
        if len(self.directory_content_list)>1:
            self.directory_content_list = [['', '', '']]

        for i in data_list:
            tmp_list = []
            file = directory_path+"/"+i
            bundle = heka_reader.Bundle(file)
            tmp_list = OnlineAnalysisManager().update_data_structure([],bundle,treeview, tmp_list) # maybe it's good to end the list at series level


            for z in range(len(tmp_list)):

                if("Group" in tmp_list[z][0]):
                    tmp_list[z][0]="Group"+i
                    tmp_list[z][1]=i


                if "Pulsed" not in tmp_list[z][0]:
                    self.directory_content_list.append(tmp_list[z])

        tree = OnlineAnalysisManager().built_tree_from_list(treeview,self.directory_content_list,0)
        self.dat_files = directory_path
        return data_list, self.dat_files, tree

    def get_parent_pos(self,start_index,list):
        for d in range(start_index,-1,-1):
            print(list[d][0])
            if "Group" in list[d][0]:
                return d

    def get_series_specific_treeview(self,treeview,series_name):
        series_specific_treeview_list = [["","",""]]
        prvs_parent_pos = -1
        for d in self.directory_content_list:
            if d[1]==series_name:
                start_index = self.directory_content_list.index(d)

                # append parent
                parent_pos = self.get_parent_pos(start_index,self.directory_content_list)
                if parent_pos != prvs_parent_pos:
                    series_specific_treeview_list.append(self.directory_content_list[parent_pos])
                    prvs_parent_pos = parent_pos

                # append the childs
                series_elements = self.get_number_of_series_elements(start_index+1, self.directory_content_list) - start_index
                for z in range(0,series_elements+1):
                    lst_ps= start_index+z
                    series_specific_treeview_list.append(self.directory_content_list[lst_ps])

        try:
            return series_specific_treeview_list, OnlineAnalysisManager().built_tree_from_list(treeview,series_specific_treeview_list,0)
        except Exception as e:
            print(e.args)



    def get_available_series_names(self,file_content_list = None):
        '''loop through all items of a given list and return all series names without name duplciates
        @input  file_content_list: a list of triples with group, series, sweeps and traces
        @return a list of strings with found series names '''

        if not file_content_list:
            file_content_list=self.directory_content_list

        list_of_series = []
        for i in file_content_list:
            if "Series" in i[0]:
                print(i[0])
                print(i[1])
                if not i[1] in list_of_series:
                    list_of_series.append(i[1])

        print(list_of_series)
        return list_of_series




    def get_multiple_series_data(self,list_of_series,file_content_list=None):
        '''  A function to extract data traces of defined series (defined in list_of_series) .dat files (represented as file_content_list) in a selected directory.
         @input list_of_series: a list of one or more series names string representated
         @return data_list: list of triples [file_name, series_name, sweep, [data_array]]
         @author dz
         @TODO : How to deal with duplicates (e.g. multiple series blockpuls) '''

        if not file_content_list:
            file_content_list = self.directory_content_list

        data_list = [] #to be filled in this function and eventually returned

        for i in list_of_series: # loop through the selected series names (strings)

            for d in file_content_list: # loop through the list of nodes (groups,series,sweeps,...)
                ''' - loop through the list, stop whenever the searched series identifier was found'''
                if d[1]==i: # string comparisson
                   series_position = file_content_list.index(d)
                   # @TODO check for the last element (-1 return)
                   next_series_position = self.get_number_of_series_elements(series_position+1,file_content_list)

                   # get the group the series belongs to (in directory view this is the filename)
                   # go backward from the current series position and choose the first group that will be found
                   for z in range(series_position,-1,-1):

                       if "Group" in file_content_list[z][0]:

                         group_name =  file_content_list[z][1]
                         group_position = z

                         next_group_position = self.get_next_group_position(group_position+1,file_content_list)

                         # check the number of series in the intersection of this group ( one group = one specific .dat file)
                         if next_group_position > 0:
                            series_in_file = OnlineAnalysisManager().get_list_of_series_names(
                                file_content_list[group_position:next_group_position])
                            series_identifiers_in_file = OnlineAnalysisManager().get_list_of_series_identifiers(file_content_list[group_position:next_group_position])
                         else:
                             series_in_file = OnlineAnalysisManager().get_list_of_series_names(
                                 file_content_list[group_position:len(file_content_list)])
                             series_identifiers_in_file = OnlineAnalysisManager().get_list_of_series_identifiers(
                                 file_content_list[group_position:len(file_content_list)])

                         file = [self.dat_files + "/" + group_name]
                         appearance = series_in_file.count(i)
                         if appearance > 1:
                             series_indices = [s for s, x in enumerate(series_in_file) if x == i]
                             for s in series_indices:
                                 series_ident = series_identifiers_in_file[s]
                                 found_series = []
                                 found_series = [s for s, x in enumerate(data_list) if (x[0] == group_name and x[1]==i and x[2]==series_ident)]
                                 if not found_series:
                                     series_pos = s
                                     break
                         else:
                            series_pos = series_in_file.index(i)

                         # open the file and read the data
                         bundle = heka_reader.Bundle(file[0])

                         if next_series_position<0:
                             next_series_position = len(file_content_list)
                         end_val = (next_series_position-series_position-1)//3   # division with 3 because of strcuture: Sweep, Imon, Ileak, Sweep, ...


                         for sweep in range(0,end_val+1):
                             source_array = [0, series_pos, sweep, 0]  # - 1 needed here since Series 1 is at position 0
                             try:
                                data_list.append([group_name,i,series_identifiers_in_file[series_pos],bundle.data[source_array]])
                             except:
                                debug = 1


                         data_length = len(data_list[len(data_list)-1][3])
                         time = np.linspace(0, data_length - 1, data_length)
                         data_list.append([group_name,series_identifiers_in_file[series_pos],"Time",time])
                         break


        return data_list

    # @TODO use instead get_series_amount_of_list_elements(self,list,series_list_index):
    def get_number_of_series_elements(self,start_index,list):
        ''' helper function to return the number of list elements of a series
        @input:     start_index:    integer value where to start to iterate
                    list:           the list with the node series elements
        @return     if a successor series was found, the last index before successor will be returned otherwise -1,
                    right now you have subtract start index and found index manually
        '''
        for i in range(start_index,len(list)):
            if "Series" in list[i][0]:
                return i-1

        return -1

    def check_for_multiple_series_in_a_file(self,node_list,series_list):
        ''' From given series names list all files will be scanned for multiple appearences of one of the series specified in the series list.
            @input  node_list: list of triples
                    series_list: list of series names (strings) the user has selected
            @return True if a series was found multiple times, False if not'''

        for a in series_list:
            for b in node_list:
                if "Group" in b[0]:
                    tmp_group_pos = node_list.index(b)
                    next_group_pos = self.get_next_group_position(tmp_group_pos+1,node_list)
                    if next_group_pos >0:
                        sub_list = node_list[tmp_group_pos:next_group_pos]
                        series_names = OnlineAnalysisManager.get_list_of_series_names(sub_list)
                    else:
                        series_names = OnlineAnalysisManager.get_list_of_series_names(
                            node_list[tmp_group_pos:len(node_list)])
                    cnt = 0
                    for s in series_names:
                        if s == a:
                            cnt = cnt+1

                    if cnt > 1:
                        return True

        return False


    def get_next_group_position(self,start_index,list):
        ''' helper function to return the index of the next group in a given list
        @input:     start_index:    integer value where to start to iterate
                    list:           the list with the series, group and sweep elements
        @return     if a successor group was found, the last index before successor will be returned otherwise -1
        '''
        for i in range(start_index,len(list)):
            if "Group" in list[i][0]:
                return i

        return -1

    def package_list(self, dat_path):
        if  isinstance(dat_path, str):
            self.data_list = os.listdir(dat_path)
            self.data = [i for i in self.data_list if ".dat" in i]
            return self.data
