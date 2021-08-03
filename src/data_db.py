import sqlite3
import os
import datetime
import re
import raw_analysis as ra
import heka_reader
import numpy as np
import io
import logging
import datetime
class DataDB():
    ''' A class to handle all data in a sqlite3 generated during offline analysis.
     @date: 23.06.2021, @author dz'''
    # /home/zida20/Desktop/Promotion/SoftwareProjekte/Etools/src/analysis_database.db

    def __init__(self):
        self.database = None
        self.analysis_id = None

        # logger settings
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('../Logs/database_manager.log')
        print(file_handler)
        formatter  = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.info('Database Manager Initialized')

    """---------------------------------------------------"""
    """ General database functions                        """
    """---------------------------------------------------"""

    def adapt_array(self,arr):
        out = io.BytesIO()
        np.save(out, arr)
        out.seek(0)
        return sqlite3.Binary(out.read())

    def convert_array(self,text):
        out = io.BytesIO(text)
        out.seek(0)
        return np.load(out)

    def create_analysis_database(self):
        self.db_file_name = "analysis_database.db"

        cew = os.getcwd()
        dir_list = os.listdir(cew)

        # Converts np.array to TEXT when inserting
        sqlite3.register_adapter(np.ndarray, self.adapt_array)

        # Converts TEXT to np.array when selecting
        sqlite3.register_converter("array", self.convert_array)

        if self.db_file_name in dir_list:
            self.logger.info("Established connection to existing database: %s ", self.db_file_name)
        else:
            self.logger.info("A new database was created. Created and Connected to new database: %s", self.db_file_name)

        try:
            self.database = sqlite3.connect(cew + "/" + self.db_file_name, detect_types=sqlite3.PARSE_DECLTYPES)
        except Exception as e:
            self.logger.info("An error occured during database initialization. Error Message: %s", e)

    ""

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
                                        analysis_id integer,
                                        foreign key (analysis_id) references offline_analysis (analysis_id)
                                    ); """

        sql_create_series_table = """ CREATE TABLE IF NOT EXISTS analysis_series (
                                                   analysis_series_name text,
                                                   time array,
                                                   recording_mode text,
                                                   analysis_id integer, 
                                                   foreign key (analysis_id) references offline_analysis (analysis_id)
                                                   primary key (analysis_series_name, analysis_id)
                                               ); """

        sql_create_experiments_table = """CREATE TABLE IF NOT EXISTS experiments (
                                               experiment_name text PRIMARY KEY,
                                               meta_data_group text,
                                               labbook_id integer,
                                               image_directory text
                                           );"""


        sql_create_sweeps_table = """ CREATE TABLE IF NOT EXISTS sweeps(
                                               sweep_id integer PRIMARY KEY autoincrement,
                                               experiment_name text, 
                                               series_identifier text,
                                               sweep_number integer,
                                               meta_data array,
                                               pgf_information text,
                                               data_array array,
                                               foreign key (experiment_name) references experiments (experiment_name) 
                                               UNIQUE(experiment_name, series_identifier, sweep_number)
                                           ); """

        #UNIQUE(experiment_name, series_identifier, sweep_number)

        sql_create_analysis_function_table = """ CREATE TABLE IF NOT EXISTS analysis_functions(
                                            analysis_function_id integer PRIMARY KEY autoincrement, 
                                            function_name text,
                                            lower_bound float,
                                            upper_bound float,
                                            analysis_series_name text,
                                            analysis_id,
                                            foreign key (analysis_series_name) references analysis_series (analysis_series_name)
                                            foreign key (analysis_id) references offline_analysis (analysis_id)
                                            );"""

        sql_create_results_table = """ CREATE TABLE IF NOT EXISTS results(
                                            analysis_function_id integer,
                                            sweep_id references sweeps,
                                            result_value,
                                            foreign key (analysis_function_id) references analysis_functions (analysis_function_id)
                                            ); """

        sql_create_experiment_series_table = """ CREATE TABLE IF NOT EXISTS experiment_series(
                                             experiment_name text,
                                             series_name,
                                             series_identifier,
                                             discarded,
                                             foreign key (experiment_name) references experiments (experiment_name),
                                             primary key (experiment_name,series_name,series_identifier)
                                             ); """

        sql_create_mapping_table = """  create table if not exists experiment_analysis_mapping(
                                        experiment_name text,
                                        analysis_id integer,
                                        foreign key (experiment_name) references experiments (experiment_name), 
                                        foreign key (analysis_id) references offline_analysis (analysis_id),
                                        UNIQUE (experiment_name, analysis_id) 
                                        ); """

        self.database = self.execute_sql_command(self.database, sql_create_offline_analysis_table)
        self.database = self.execute_sql_command(self.database, sql_create_filter_table)
        self.database = self.execute_sql_command(self.database, sql_create_series_table)
        self.database = self.execute_sql_command(self.database, sql_create_experiments_table)
        self.database = self.execute_sql_command(self.database, sql_create_sweeps_table)
        self.database = self.execute_sql_command(self.database, sql_create_analysis_function_table)
        self.database = self.execute_sql_command(self.database, sql_create_results_table)
        self.database = self.execute_sql_command(self.database, sql_create_experiment_series_table)
        self.database = self.execute_sql_command(self.database, sql_create_mapping_table)

    # @todo refactor to write to database
    def execute_sql_command(self,database,sql_command,values = None):
        try:
            tmp = database.cursor()
            if values:
                tmp.execute(sql_command,values)
                #self.logger.info("Execute SQL Command: %s with values %s", sql_command,values)
            else:
                tmp.execute(sql_command)
                #self.logger.info("Execute SQL Command: %s without values", sql_command)
            database.commit()
            return database
        except Exception as e:
                self.logger.error("Error in Execute SQL Command: %s",e)
                return database

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

    """--------------------------------------------------------------"""
    """ Functions to interact with table experiment_analysis_mapping """
    """--------------------------------------------------------------"""

    def create_mapping_between_experiments_and_analysis_id(self,experiment_name):
        q = f'insert into experiment_analysis_mapping values (?,?)'
        self.database = self.execute_sql_command(self.database, q, (experiment_name,self.analysis_id))

    """---------------------------------------------------"""
    """ Functions to interact with table offline_analysis """
    """---------------------------------------------------"""

    def insert_new_analysis(self,user):
        q = """insert into offline_analysis (date_time, user) values (?,?) """
        time_stamp = datetime.datetime.now()
        self.database = self.execute_sql_command(self.database, q, (time_stamp,user))
        self.logger.info("Started new Analysis for user %s at time %s", user, time_stamp)

        q = """select analysis_id from offline_analysis where date_time = (?) AND user = (?) """
        self.analysis_id = self.get_data_from_database(self.database,q,(time_stamp,user))[0][0]
        self.logger.info("Analysis id for this analysis will be: %s", self.analysis_id)
        return self.analysis_id



    """---------------------------------------------------"""
    """    Functions to interact with table filters       """
    """---------------------------------------------------"""

    def write_filter_into_database(self,filter_name,lower_threshold,upper_threshold):
        q = """ insert into filters values (?,?,?,?)"""
        self.database = self.execute_sql_command(self.database,q,(filter_name,lower_threshold,upper_threshold,self.analysis_id))


    """---------------------------------------------------"""
    """    Functions to interact with table analysis_series     """
    """---------------------------------------------------"""

    def write_analysis_series_types_to_database(self, name_list):
        '''Takes the user selected series types (e.g. block pulse, iv, ...) and places them in the referring database
        table "series"
        @date: 23.06.2021, @author: dz '''

        for n in name_list:
            q = f'INSERT INTO analysis_series (analysis_series_name,analysis_id) VALUES (?,?) '
            self.database = self.execute_sql_command(self.database,q,(n,self.analysis_id))
            print("inserting new analysis_series with id", self.analysis_id)
        print ("inserted all series")

    def write_ms_spaced_time_array_to_analysis_series_table(self,time_np_array, analysis_series_name, analysis_id ):
        """

        :param time_np_array: time in milliseconds already converted into numpy array
        :return:
        """
        q = 'update analysis_series set time = (?) where analysis_series_name = (?) AND analysis_id = (?)'
        self.database = self.execute_sql_command(self.database,q,(time_np_array,analysis_series_name,analysis_id))

    def write_recording_mode_to_analysis_series_table(self,recording_mode,analysis_series_name,analysis_id):
        q = 'update analysis_series set recording_mode = (?) where analysis_series_name = (?) AND analysis_id = (?)'
        self.database = self.execute_sql_command(self.database,q,(recording_mode,analysis_series_name,analysis_id))

    def get_time_in_ms_of_analyzed_series(self,series_name):
        q = """select time from analysis_series where analysis_series_name = (?) AND analysis_id = (?)"""
        res =  self.get_data_from_database(self.database,q,(series_name,self.analysis_id))[0][0]
        return res

    """---------------------------------------------------"""
    """    Functions to interact with table experiments    """
    """---------------------------------------------------"""

    def add_experiment_to_experiment_table(self,name,meta_data_group = None,series_name = None,mapping_id=None):
        q = f'insert into experiments (experiment_name) select (\"{name}\") where not exists (select 1 from experiments where experiment_name == \"{name}\" )'
        self.database = self.execute_sql_command(self.database, q)

    """---------------------------------------------------"""
    """    Functions to interact with table experiment_series    """
    """---------------------------------------------------"""

    def add_single_series_to_database(self,experiment_name,series_name,series_identifier):
        # trying to insert - could fail if unique constraint fails
        q = """insert or replace into experiment_series values (?,?,?,?) """
        self.database = self.execute_sql_command(self.database,q,(experiment_name,series_name, series_identifier,0))



    """----------------------------------------------------------"""
    """    Functions to interact with table analysis_functions   """
    """----------------------------------------------------------"""
    ###

    def write_analysis_function_name_and_cursor_bounds_to_database(self,analysis_function, analysis_series_name,lower_bound,upper_bound):
      q = """insert into analysis_functions (function_name, analysis_series_name, analysis_id,lower_bound,upper_bound) values (?,?,?,?,?)"""
      self.database = self.execute_sql_command(self.database,q,(analysis_function,analysis_series_name,self.analysis_id,lower_bound,upper_bound))

    def get_last_inserted_analysis_function_id(self):
      q = """select analysis_function_id from analysis_functions """
      id_list = self.get_data_from_database(self.database,q)
      print("greatest identifier is: ", max(id_list)[0])
      return max(id_list)[0]


    def get_series_specific_analysis_funtions(self,series_name):
        q = """ select distinct function_name 
        from analysis_functions where analysis_series_name = (?) AND analysis_id = (?) """
        r = self.get_data_from_database(self.database,q,(series_name, self.analysis_id))
        function_list = []
        for t in r:
            function_list.append(t[0])
        return function_list

    def get_cursor_bounds_of_analysis_function(self,function_name,series_name):
        """
        Returns a list triples (lower, upper bound, id) for the specified analysis function name and the analysis id.
        :param function_name: name of the analysis function (e.g. min, max, .. )
        :param series_name: name of the analysis series (e.g. Block Pulse, ... )
        :return: a list of cursor bound triples, with cursor bound values at positions 0 and 1 and the
        function analysis id at the third position
        """

        q = """select lower_bound, upper_bound, analysis_function_id 
        from analysis_functions where function_name = (?) AND analysis_series_name=(?) AND analysis_id = (?)"""
        r = self.get_data_from_database(self.database,q,(function_name,series_name,self.analysis_id))
        cursor_bounds = []
        for t in r:
            cursor_bounds.append(t)
        return cursor_bounds


    """----------------------------------------------------------"""
    """    Functions to interact with table sweeps   """
    """----------------------------------------------------------"""

    def get_single_sweep_data_from_database_by_sweep_id(self,sweep_id):
        q = f'select data_array from sweeps where sweep_id = \"{sweep_id}\"'
        return self.get_data_from_database(self.database,q)[0][0]



    def get_sweep_id_list_for_offline_analysis(self,series_name):
        """
        returns a list of id's of sweeps to be analyzed for this sepcific series name and analysis_id
        :param series_name:
        :return:
        """
        q = """select r.sweep_id from (select s.experiment_name, s.series_identifier, s.sweep_id from sweeps s inner join 
        experiment_analysis_mapping m where s.experiment_name = m.experiment_name AND m.analysis_id = (?)) r inner join 
        experiment_series es where r.experiment_name = es.experiment_name AND r.series_identifier = es.series_identifier 
        AND es.series_name = (?) ;"""
        sweep_id_tuples = self.get_data_from_database(self.database,q,(self.analysis_id,series_name))
        sweep_id_list = []
        for t in sweep_id_tuples:
            sweep_id_list.append(t[0])
        return sweep_id_list



    def get_sweep_meta_data(self,datalist,pos):
        """ write dictionary to array in database """

        data = datalist[pos + 1][2][0]
        data = list(data.items())

        return np.array(data)



    def write_analysis_function_to_database(self,function_list,series_type):
        for f in function_list:
            sql_command = """INSERT INTO analysis_functions (function_name,series_type) VALUES (?,?) """
            self.database = self.execute_sql_command(self.database, sql_command,(f,series_type))

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


    def calculate_single_series_results_and_write_to_database(self,series_type):
        q = f'select s.sweep_id, s.data_array from  sweeps s inner join experiments e on  s.experiment_name = e.experiment_name AND e.series_name = \"{series_type}\";'# [sweep_id, sweep_data_trace]
        sweeps = self.get_data_from_database(self.database,q)

        q = f'select id,function_name,lower_coursor,upper_coursor from analysis_functions where series_type = \"{series_type}\";' # [anlysis_id,analysis_function,lower_bound,upper_bound]
        analysis_functions = self.get_data_from_database(self.database,q)

        q = f'select time from analysis_series where analysis_series_name = \"{series_type}\";'
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


    # Still used ?
    def read_trace_data_and_write_to_database(self,series_type,data_path):
        ''' function to read data arrays of each sweep and write it to the sweeps table in the database, arrays are represented as strings'''

        q = f'SELECT experiment_name FROM experiments WHERE series_name = \"{series_type}\";'
        file_names = self.get_data_from_database(self.database,q)

        q = f'select time from analysis_series where analysis_series_name = \"{series_type}\";'
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

                   q = """update analysis_series set time = (?) where analysis_series_name = (?);"""
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


    def add_sweep_to_sweep_table(self,experiment_name,tmp_list,current_object):

        p = tmp_list.index(current_object)
        # extract sweep_number
        sweep_number = self.get_sweep_number(current_object[0])
        # extract series_identifier
        series_identifier = self.get_series_identifier(tmp_list,p)
        # extract meta_data_string
        meta_data = self.get_sweep_meta_data(tmp_list,p)

        q = "insert into sweeps (experiment_name, series_identifier, sweep_number,meta_data) values (?,?,?,?)"
        self.database = self.execute_sql_command(self.database, q,(experiment_name,series_identifier,sweep_number,meta_data))

        #def add_series_to_experiment_series(self, experiment_name, tmp_list):

    def add_single_sweep_tp_database(self,experiment_name,series_identifier,sweep_number,meta_data,data_array):
        np_data_array = np.array(data_array)

        d = meta_data[0].get_fields()
        l = list(d.items())
        np_meta_data = np.array(l)

        q = "insert into sweeps (experiment_name, series_identifier, sweep_number,meta_data,data_array) values (?,?,?,?,?)"
        self.database = self.execute_sql_command(self.database, q,
                                                 (experiment_name, series_identifier, sweep_number, np_meta_data, np_data_array))


    def get_single_sweep_meta_data_from_database(self,data_array):
        """
        returns the meta data array for a specific sweep
        :param data_array: data array with 3 fields (experiment_name, series_identifier, sweep_number)
        :return: meta data array (numpy array)
        """

        # since the meta_data object is a a list of list, numpy will save it as object (narray)
        # therefore, the object is "pickled" into a byte stream and unpickled from byte stream into an object.
        # loaded pickled data seem to be able  to execute arbitrary code - for safety reasons pickling is therefore
        # disabled and needs to be enabled for the specific unpickle of meta data byte stream
        np.load.__defaults__ = (None, True, True, 'ASCII')
        res = self.get_single_sweep_parameter_from_database(data_array, "meta_data")

        # finally disable pickle again
        np.load.__defaults__ = (None, False, True, 'ASCII')
        return res

    def get_single_sweep_data_from_database(self,data_array):
        """
        returns the data array for a specific sweep
        :param data_array: data array with 3 fields (experiment_name, series_identifier, sweep_number)
        :return: data array (numpy array)
        """

        return self.get_single_sweep_parameter_from_database(data_array,"data_array")

    def get_single_sweep_parameter_from_database(self,data_array,parameter):
        """
        performs a database request on the sweep table to get the value for the specified parameter.
        To make sure that only series names available in the selected experiments therefore a join with experiment
        table considering the current analysis id will be performed.
        :param data_array: data array with 3 fields (experiment_name, series_identifier, sweep_number)
        :param parameter: string represenation of the paramter (==column name)
        :return: value of the requested parameter
        """

        # variable declaration not needed - just here to increase code readability
        experiment_name = data_array[0]
        series_identifier = data_array[1]
        sweep_number = data_array[2]

        q = f'SELECT {parameter} FROM sweeps WHERE experiment_name == \"{experiment_name}\"  AND series_identifier == \"{series_identifier}\" AND sweep_number == \"{sweep_number}\";'
        res = self.get_data_from_database(self.database, q)
        return res[0][0]

    def discard_specific_series(self, experiment_name, series_name, series_identifier):
        """Change the column valid for a specifc series from 0 (valid) to 1 (discarded, in-valid)"""
        self.change_experiment_series_discarded_state(experiment_name, series_name, series_identifier, 1)

    def reinsert_specific_series(self,experiment_name,series_name,series_identifier):
        self.change_experiment_series_discarded_state(experiment_name, series_name, series_identifier, 0)

    def change_experiment_series_discarded_state(self,experiment_name,series_name,series_identifier,state):
        q = """update experiment_series set discarded = (?) where experiment_name = (?) AND series_name = (?) AND series_identifier = (?);"""
        res = self.execute_sql_command(self.database, q, (state, experiment_name, series_name, series_identifier))


    def get_distinct_non_discarded_series_names(self):

        q = """select distinct series_name from experiment_series where "discarded" == 0"""
        return self.get_data_from_database(self.database,q)


 ###### deprecated ######

 # @todo deprecated ?
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
    '''
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
    '''