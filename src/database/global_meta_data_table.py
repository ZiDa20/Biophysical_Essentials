class GlobalMetaDataTable():

    """---------------------------------------------------"""
    """    Functions to interact with table global_meta_data    """
    """---------------------------------------------------"""

    def __init__(self, database=None, analysis_id=None, logger=None):
        self.database = database
        self.analysis_id = analysis_id
        self.logger = logger

    def add_experiment_to_global_meta_data(self, id, meta_data):
        q = f'insert into global_meta_data (analysis_id,experiment_name, experiment_label, species, genotype, sex, condition, individuum_id) values ' \
            f'({id},\'{meta_data[0]}\',\'{meta_data[1]}\',\'{meta_data[2]}\',\'{meta_data[3]}\',\'{meta_data[4]}\',\'{meta_data[5]}\',\'{meta_data[6]}\' )'
        try:
            self.database = self.execute_sql_command(self.database, q)
            self.logger.info(meta_data[0], "added succesfully to global_meta_data")
            return 1
        except Exception as e:
            if "Constraint Error" in str(e):
                self.logger.info(
                    "Experiment with name %s was already in global meta data")
            else:
                print("adding experiment to global meta data failed")

    def get_available_experiment_label(self):
        """
        return all available label in the database
        @return: a tuple list
        """
        q = f'select distinct experiment_label from global_meta_data'
        res = self.get_data_from_database(self.database, q)
        return res

    def get_meta_data_group_of_specific_experiment(self, experiment_name):
        """
        :param experiment_name:
        :return:
        :author dz, 28.06.2022
        """
        q = f'select condition from global_meta_data where experiment_name = \'{experiment_name}\''
        return self.get_data_from_database(self.database, q)[0][0]

    def add_meta_data_group_to_existing_experiment(self, meta_data_list: list):
        """
        Insert meta data group into an exsiting experiment
        :param meta_data_list: [0]: experiment_name, [1]: experiment_label, [2] = species, [3] =
        :return:
        """

        q = f'update global_meta_data set experiment_label = \'{meta_data_list[1]}\',' \
            f'species = \'{meta_data_list[2]}\', genotype = = \'{meta_data_list[3]}\', sex = \'{meta_data_list[4]}\',' \
            f'condition = \'{meta_data_list[5]}\',individuum_id = \'{meta_data_list[6]}\' where experiment_name = \'{meta_data_list[0]}\''
        try:
            self.database = self.execute_sql_command(self.database, q)
            self.logger.info(f'Wrote meta data for experiment \'{meta_data_list[0]}\' into database"')
            return True
        except Exception as e:
            self.logger.info(
                f'FAILED to write meta data for experiment \'{meta_data_list[0]}\' into database with error {str(e)}')
            return False

    def get_meta_data_of_multiple_experiments(self):
        """
        @todo DZ add description .. implemented during load finished analysis
        @return:
        """
        q = f'select experiment_name from global_meta_data intersect (select experiment_name from experiment_analysis_mapping where analysis_id = {self.analysis_id})'
        experiment_names = self.get_data_from_database(self.database, q)

        meta_data = []
        for name in experiment_names:
            q = f'select condition from global_meta_data where experiment_name = \'{name[0]}\''
            meta_data.append(self.database.execute(q).fetchall()[0][0])

        return meta_data

        # @todo refactor to write to database

    def execute_sql_command(self, database, sql_command, values=None):
        try:
            if values:
                self.database.execute(sql_command, values)
                # self.logger.info("Execute SQL Command: %s with values %s", sql_command,values)
            else:
                self.database.execute(sql_command)
                # self.logger.info("Execute SQL Command: %s without values", sql_command)
            self.database.commit()
            return self.database
        except Exception as e:
            self.print("Error in Execute SQL Command: %s", e)
            #self.logger.error("Error in Execute SQL Command: %s", e)
            raise Exception(e)

    def get_data_from_database(self, database, sql_command, values=None, fetch_mode=None):
        try:
            # tmp = database.cursor()
            if values:
                self.database.execute(sql_command, values)
            else:
                self.database.execute(sql_command)
            if fetch_mode is None:
                return self.database.fetchall()
            if fetch_mode == 1:
                return self.database.fetchnumpy()
            if fetch_mode == 2:
                return self.database.fetchdf()
        except Exception as e:
            print(e)