import sqlite3
import os
import datetime
import re
import raw_analysis as ra
import heka_reader
import numpy as np

class DataDB():
    ''' A class to handle all data in a sqlite3 generated during offline analysis.
     @date: 23.06.2021, @author dz'''
    # /home/zida20/Desktop/Promotion/SoftwareProjekte/Etools/src/analysis_database.db

    def __init__(self):
        self.database = None
        self.offline_analysis_id = None

    def create_analysis_database(self):
        self.db_file_name = "analysis_database.db"

        cew = os.getcwd()
        dir_list = os.listdir(cew)
        if self.db_file_name in dir_list:
            os.remove(cew + "/" + self.db_file_name)
        try:
            self.database = sqlite3.connect(cew + "/" + self.db_file_name)
        except Exception as e:
            print(e)


    def create_database_tables(self):
        '''Create all database tables if they do not exist'''

        sql_create_offline_analysis_table = """ CREATE TABLE IF NOT EXISTS offline_analysis (
                                                analysis_id integer PRIMARY KEY autoincrement,
                                                date_time,
                                                user
                                                ); """

        sql_create_filter_table = """ CREATE TABLE IF NOT EXISTS filters (
                                        filter_criteria_name primary key,
                                        lower_threshold float,
                                        upper_threshold float,
                                        analysis_id integer references offline_analysis
                                    ); """

        sql_create_series_table = """ CREATE TABLE IF NOT EXISTS series (
                                                   name text primary key,
                                                   time,
                                                   recording_mode,
                                                   analysis_id references offline_analysis
                                               ); """

        sql_create_experiments_table = """CREATE TABLE IF NOT EXISTS experiments (
                                               name text,
                                               meta_data_group text,
                                               series_name text references series
                                           );"""

        # @TODO sqlite does not support arrays -> therefore arrays will be safed as large strings as a workaround
        sql_create_sweeps_table = """ CREATE TABLE IF NOT EXISTS sweeps(
                                               sweep_id integer PRIMARY KEY autoincrement,
                                               experiment_name references experiments,
                                               series_identifier text,
                                               sweep_number integer,
                                               meta_data text,
                                               pgf_information text,
                                               data_array text
                                           ); """

        sql_create_analysis_function_table = """ CREATE TABLE IF NOT EXISTS analysis_functions(
                                            id integer PRIMARY KEY autoincrement, 
                                            function_name text,
                                            lower_coursor integer,
                                            upper_coursor integer,
                                            series_type references series
                                            );"""

        sql_create_results_table = """ CREATE TABLE IF NOT EXISTS results(
                                            analysis_id references analysis_functions,
                                            sweep_id references sweeps,
                                            result_value
                                            ); """

        self.database = self.execute_sql_command(self.database, sql_create_offline_analysis_table)
        self.database = self.execute_sql_command(self.database, sql_create_filter_table)
        self.database = self.execute_sql_command(self.database, sql_create_series_table)
        self.database = self.execute_sql_command(self.database, sql_create_experiments_table)
        self.database = self.execute_sql_command(self.database, sql_create_sweeps_table)
        self.database = self.execute_sql_command(self.database, sql_create_analysis_function_table)
        self.database = self.execute_sql_command(self.database, sql_create_results_table)

    # @todo refactor to write to database
    def execute_sql_command(self,database,sql_command,values = None):
        try:
            tmp = database.cursor()
            if values:
                tmp.execute(sql_command,values)
            else:
                tmp.execute(sql_command)

            database.commit()
            return database
        except Exception as e:
            print(e)

    def get_data_from_database(self,database,sql_command,values=None):
        try:
            tmp = database.cursor()
            if values:
                tmp.execute(sql_command,values)
            else:
                tmp.execute(sql_command)

            return tmp.fetchall()
        except Exception as e:
            print(e)


    def write_filter_into_database(self,filter_name,lower_threshold,upper_threshold):
        q = """ insert into filters values (?,?,?,?)"""
        self.database = self.execute_sql_command(self.database,q,(filter_name,lower_threshold,upper_threshold,self.offline_analysis_id))

    def write_analysis_series_types_to_database(self, name_list):
        '''Takes the user selected series types (e.g. block pulse, iv, ...) and places them in the referring database
        table "series". If no id has been given to this analysis yet, a new id will be automatically generated by inserting the
        timestamp of this analysis into the offline analysis table. The gobal value of self.offline_analysis_id will be modified
        therefore.
        @date: 23.06.2021, @author: dz '''

        if  self.offline_analysis_id is None:
            analysis_time = datetime.datetime.now()
            q = f'insert into offline_analysis (date_time) values (\"{analysis_time}\")'
            self.database = self.execute_sql_command(self.database,q)
            q = f'select analysis_id from offline_analysis where date_time = \"{analysis_time}\"'
            id = self.get_data_from_database(self.database,q)
            self.offline_analysis_id = id[0][0]

        for n in name_list:
            q = f'INSERT INTO series (name,analysis_id) VALUES (?,?) '
            self.database = self.execute_sql_command(self.database,q,(n,self.offline_analysis_id))
        print ("inserted all series")

    def fill_database_from_treeview_list(self,data_list,series_type):
        ''' Function to read the list which was created to built the treeview in the frontend - this data list will be reused and
          it's data will be stored into the experiments or sweep table in the database.
          Furthermore the recording mode of the series type will be extracted and will be stored in the series table in
          column recording mode @date 23.06.2021, @author dz '''

        q = f'select recording_mode from series where name=\"{series_type}\"'
        rec_mode = self.get_data_from_database(self.database,q)


        # to avoid second insertation: once the rec mode was written, data have been also inserted at least once

        test = rec_mode[0]
        if rec_mode[0][0] is None:

            for d in data_list:
                if "Group" in d[0]:
                    sql_command = """INSERT INTO experiments VALUES (?,?,?)"""
                    values = (d[1], "control",series_type)
                    self.database = self.execute_sql_command(self.database,sql_command,values)

                if "Sweep" in d[0]:
                    experiment_number = self.get_sweep_parent(data_list,data_list.index(d))
                    meta_data = self.get_sweep_meta_data(data_list,data_list.index(d))

                    trace_rec_mode = str(data_list[data_list.index(d)+1][2][0].get_fields()["RecordingMode"])
                    if rec_mode[0][0] is None:
                        q = f'update series set recording_mode = (?) where name = (?)'
                        if trace_rec_mode == "b'\\x03'":
                            values = ("Voltage Clamp",series_type)
                            rec_mode[0] = ("Voltage Clamp",)
                        else:
                            values = ("Current Clamp",series_type)
                            rec_mode[0] = ("Current Clamp",)

                        self.database = self.execute_sql_command(self.database, q, values)

                    series_identifier = self.get_series_identifier(data_list,data_list.index(d))
                    sweep_number = self.get_sweep_number(d[0])

                    sql_command = "insert into sweeps (experiment_name,series_identifier,sweep_number,meta_data) values(?,?,?,?);"
                    values = (experiment_number,series_identifier,sweep_number,meta_data)

                    self.database = self.execute_sql_command(self.database,sql_command,values)

    def get_sweep_meta_data(self,datalist,pos):
        # the list entry after the sweeps positions (pos) holds the data trace
        # since sqlite does not allow array insertion, a string will be generated
        # data points will be separated by comma (,)

        data = datalist[pos+1][2][0].get_fields()
        data_string = ""
        for key,value in data.items():
            if type(value) != str:
                value = str(value)

            data_string = data_string + "(" + key + ","+ value + "),"

        return data_string


    def get_sweep_parent(self,datalist,pos):
        ''' returns experiment name as a string,
        type: internal helper_function, author: dz, 15.06.21 '''
        return self.find_node_type(datalist, pos, "Group",1)

    def get_series_identifier(self,datalist,pos):
        ''' returns series identifier name as a string,
        type: internal helper_function, author: dz, 15.06.21 '''

        return self.find_node_type(datalist,pos,"Series",0)


    def find_node_type(self,datalist,pos,type,elem):
        '''type: internal helper_function, author: dz, 15.06.21 '''
        for d in range(pos,-1,-1):
            if type in datalist[d][0]:
                return datalist[d][elem]

    def get_sweep_number(self,sweep_name):
        '''get the sweep number out of a string,
        type: internal helper_function, author: dz, 15.06.21 '''

        splitted_string = re.match(r"([a-z]+)([0-9]+)",sweep_name,re.I)
        res = splitted_string.groups()
        return(res[1])

    def write_coursor_bounds_to_database(self,lower_value,upper_value,series_name):
        '''adds the two 2 incoming values to all functions in the table.'''

        # from database: get the number of selected analysis functions
        q1 = """ SELECT function_name FROM analysis_functions """
        r1 = self.get_data_from_database(self.database,q1)
        q2 = """ select distinct function_name from analysis_functions """
        r2 = self.get_data_from_database(self.database, q2)
        zero = -1

        if len(r2) == len(r1):
            non_zero_bound = """ select lower_coursor from analysis_functions where function_name= (?)"""
            values = (r2[0][0])
            zero  = self.execute_sql_command(self.database, non_zero_bound,values)

        if len(r2)>len(r1) or zero:
            for d in r2:
                q = """insert into analysis_functions(function_name,lower_coursor,upper_coursor) values (?,?,?)"""
                values = (d,lower_value,upper_value)
                self.database = self.execute_sql_command(self.database, q, values)
        else:
            q = """update analysis_functions set lower_coursor=(?), upper_coursor=(?) where function_name = (?) """
            for d in r2:
                values = (lower_value,upper_value,d[0])
                self.database = self.execute_sql_command(self.database, q, values)

        # from database: check if coursor bounds are empty (only when less then 2 duplicates available)

    def write_analysis_function_to_database(self,function_list,series_type):
        for f in function_list:
            sql_command = """INSERT INTO analysis_functions (function_name,series_type) VALUES (?,?) """
            self.database = self.execute_sql_command(self.database, sql_command,(f,series_type))

    def calculate_single_series_results_and_write_to_database(self,series_type):
        q = f'select s.sweep_id, s.data_array from  sweeps s inner join experiments e on  s.experiment_name = e.name AND e.series_name = \"{series_type}\";'# [sweep_id, sweep_data_trace]
        sweeps = self.get_data_from_database(self.database,q)

        q = f'select id,function_name,lower_coursor,upper_coursor from analysis_functions where series_type = \"{series_type}\";' # [anlysis_id,analysis_function,lower_bound,upper_bound]
        analysis_functions = self.get_data_from_database(self.database,q)

        q = f'select time from series where name = \"{series_type}\";'
        time = self.get_data_from_database(self.database, q)
        time = self.convert_string_to_array(time[0][0])

        for s in sweeps:
            data = self.convert_string_to_array(s[1])
            raw_analysis_class_object = ra.AnalysisRaw(time,data)

            for a in analysis_functions:
                raw_analysis_class_object.lower_bounds = a[2]
                raw_analysis_class_object.upper_bounds = a[3]

                raw_analysis_class_object.construct_trace()
                raw_analysis_class_object.slice_trace()

                res = raw_analysis_class_object.call_function_by_string_name(a[1])

                q = """ insert into results values (?,?,?) """
                self.write_result_to_database(a[0],s[0],res)

    def write_result_to_database(self,analysis_id,sweep_id,result_value):
        q = """insert into results values (?,?,?) """
        self.database = self.execute_sql_command(self.database,q,(analysis_id,sweep_id,result_value))

    def read_trace_data_and_write_to_database(self,series_type,data_path):
        ''' function to read data arrays of each sweep and write it to the sweeps table in the database, arrays are represented as strings'''

        q = f'SELECT name FROM experiments WHERE series_name = \"{series_type}\";'
        file_names = self.get_data_from_database(self.database,q)

        q = f'select time from series where series_name = \"{series_type}\";'
        time = self.get_data_from_database(self.database,q)

        for f in file_names:
            q = f'select series_identifier,sweep_number,sweep_id from sweeps where experiment_name = \"{f[0]}\";'
            sweeps = self.get_data_from_database(self.database,q)
            file_path = data_path + "/" + f[0]
            bundle = heka_reader.Bundle(file_path)
            for s in sweeps:
                series_name = s[0]
                sweep_number = s[1]
                series_number = self.get_sweep_number(series_name) # it's just the name of the function that is a little bit confusing - function is doing the right thing
                data_array = bundle.data[[0,int(series_number)-1,int(sweep_number)-1,0]]

                # when the first data are entered, time will be set once for all sweeps of the sweep table
                # before this type of time is None
                if time is None:

                   time =  np.linspace(0, len(data_array) - 1, len(data_array))
                   string_time = self.convert_array_to_string(time)

                   q = """update series set time = (?) where name = (?);"""
                   self.database = self.execute_sql_command(self.database,q,(string_time,series_type))

                # convert data array into comma separated string
                data_array = self.convert_array_to_string(data_array)

                q = """update sweeps set data_array = (?) where sweep_id = (?);"""
                self.database = self.execute_sql_command(self.database,q,(data_array,s[2]))

    def read_series_type_specific_analysis_functions_from_database(self,series_name):
        q = f'select distinct function_name from analysis_functions where series_type = \"{series_name}\" '
        res_string = self.get_data_from_database(self.database,q)
        string_list = []
        for t in res_string:
            string_list.append(t[0])
        return string_list

    def convert_string_to_array(self,array_as_string):
        sub_res = array_as_string.split(",")
        int_array = []
        for s in sub_res:
            int_array.append(float(s))

        return int_array



    def convert_array_to_string(self,data_array):
        output_string = ""
        for d in data_array:
            if output_string == "":
                output_string = str(d)
            else:
                output_string = output_string + ","  + str(d)

        return output_string
