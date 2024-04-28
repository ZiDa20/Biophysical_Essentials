import configparser


class SettingsFileHandler():
    
    def __init__(self) -> None:
        
        self.config = configparser.ConfigParser()
        self.config.read('Backend/Settings/bpe_settings.ini')

    def get_parameter(self,section_header:str, parameter_name:str):
        return self.config[section_header][parameter_name]
       
    
    def set_parameter(self,section_header:str, parameter_name:str,new_parameter_value):
        self.config[section_header][parameter_name] = new_parameter_value
        with open('Backend/Settings/bpe_settings.ini', 'w') as configfile:
            self.config.write(configfile)
        
    

    def get_bpe_database_path(self):
        return self.get_parameter("database","bpe_db_path")
    
    def set_bpe_database_path(self,new_path:str):
        self.set_parameter('database','bpe_db_path',new_path)

    def reset_bpe_database_path(self):
        self.set_parameter('database','bpe_db_path',self.get_parameter("database","bpe_db_path_default"))

    def get_bpe_database_name(self):
        return self.get_parameter("database","bpe_db_name")
    
    def set_bpe_database_name(self,new_name:str):
        self.set_parameter('database','bpe_db_name',new_name)

    def reset_bpe_database_name(self):
        self.set_parameter('database','bpe_db_name',self.get_parameter("database","bpe_db_name_default"))