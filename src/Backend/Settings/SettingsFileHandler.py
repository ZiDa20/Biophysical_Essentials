import configparser


class SettingsFileHandler():
    """
    SettingsFileHandler Handling all the permanent BPE configurations that have to stay longer than a sigle session
    The settings file is name bpe_settings.ini
    DZ, 29.04.2024
    """
    def __init__(self) -> None:
        
        self.config = configparser.ConfigParser()
        # set the permanent path to the config file
        # this path must never be changed
        self.config.read('Backend/Settings/bpe_settings.ini')

    def get_parameter(self,section_header:str, parameter_name:str):
        """
        get_parameter get a parameter from the config file

        Args:
            section_header (str): section header labes as string
            parameter_name (str): paramter name as string

        Returns:
            _type_: str
        """
        return self.config[section_header][parameter_name]
       
    
    def set_parameter(self,section_header:str, parameter_name:str,new_parameter_value):
        """
        set_parameter overrides a given parameter in the config file

        Args:
            section_header (str): section header labes as string
            parameter_name (str): paramter name as string: this parameter will be overwritten
            new_parameter_value (_type_): new value to be stored in the file
        """
        self.config[section_header][parameter_name] = new_parameter_value
        with open('Backend/Settings/bpe_settings.ini', 'w') as configfile:
            self.config.write(configfile)

    def get_bpe_database_path(self):
        """
        get_bpe_database_path get the path of the database

        Returns:
            str: path of the db
        """
        return self.get_parameter("database","bpe_db_path")
    
    def set_bpe_database_path(self,new_path:str):
        """
        set_bpe_database_path overrides the database path

        Args:
            new_path (str): new path argument
        """
        self.set_parameter('database','bpe_db_path',new_path)

    def reset_bpe_database_path(self):
        """
        reset_bpe_database_path overrides the bpe_db_path parameter with the bpe_db_path_default parameter
        """
        self.set_parameter('database','bpe_db_path',self.get_parameter("database","bpe_db_path_default"))

    def get_bpe_database_name(self):
        """
        get_bpe_database_name returns the name of the database file

        Returns:
            str: name of the database file
        """
        return self.get_parameter("database","bpe_db_name")
    
    def set_bpe_database_name(self,new_name:str):
        """
        set_bpe_database_name overrides the database name with the given value

        Args:
            new_name (str): new name as string
        """
        self.set_parameter('database','bpe_db_name',new_name)

    def reset_bpe_database_name(self):
        """
        reset_bpe_database_name overrides the bpe_db_name parameter with the bpe_db_name_default parameter
        """
        self.set_parameter('database','bpe_db_name',self.get_parameter("database","bpe_db_name_default"))