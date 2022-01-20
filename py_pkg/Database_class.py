import collections

class Database_class():
    __Database_class_instance = None

    def __init__(self):
        self.temp_database = collections.defaultdict(dict)
        

    @classmethod
    def get_Database_class_instance(cls):
        if cls.__Database_class_instance == None:
            cls.__Database_class_instance = Database_class()

        return cls.__Database_class_instance

    def store_User_Default_Table(self, user_id: str, default_mode: str, default_file_path: str=None, 
                                    default_id_column: str=None, default_data_column: str=None, default_model_name: str=None):

        self.temp_database[user_id]['User_Default_Table']['user_id'] = user_id
        self.temp_database[user_id]['User_Default_Table']['default_mode'] = default_mode
        self.temp_database[user_id]['User_Default_Table']['default_file_path'] = default_file_path
        self.temp_database[user_id]['User_Default_Table']['default_id_column'] = default_id_column
        self.temp_database[user_id]['User_Default_Table']['default_data_column'] = default_data_column
        self.temp_database[user_id]['User_Default_Table']['default_model_name'] = default_model_name
        
        return

    def get_User_Default_Table(self, user_id: str):

        user_id = self.temp_database[user_id]['User_Default_Table']['user_id']
        default_mode = self.temp_database[user_id]['User_Default_Table']['default_mode']
        default_file_path = self.temp_database[user_id]['User_Default_Table']['default_file_path']
        default_id_column = self.temp_database[user_id]['User_Default_Table']['default_id_column']
        default_data_column = self.temp_database[user_id]['User_Default_Table']['default_data_column'] 
        default_model_name = self.temp_database[user_id]['User_Default_Table']['default_model_name']

        return user_id, default_mode, default_file_path, default_id_column, default_data_column, default_model_name

    def store_User_Sponsor_Table(self, user_id: str, task_id: str, test_indicator: str, task_mode: str, model_name: str, metric_name: str, test_id: str=None, 
                                task_name: str=None, task_description: str=None, train_file_path: str=None, train_id_path: str=None, train_data_path: str=None, 
                                train_target_path: str=None, test_file_path: str=None, test_id_path: str=None, test_data_path: str=None, test_target_path: str=None):
        
        key = None
        if test_indicator == 'train':
            key = (user_id, task_id, test_indicator)
        elif test_indicator == 'test':
            key = (user_id, test_id, test_indicator)

        self.temp_database[key]['User_Sponsor_Table']['user_id'] = user_id
        self.temp_database[key]['User_Sponsor_Table']['task_id'] = task_id
        self.temp_database[key]['User_Sponsor_Table']['test_indicator'] = test_indicator
        self.temp_database[key]['User_Sponsor_Table']['task_mode'] = task_mode
        self.temp_database[key]['User_Sponsor_Table']['model_name'] = model_name
        self.temp_database[key]['User_Sponsor_Table']['metric_name'] = metric_name
        self.temp_database[key]['User_Sponsor_Table']['test_id'] = test_id
        self.temp_database[key]['User_Sponsor_Table']['task_name'] = task_name
        self.temp_database[key]['User_Sponsor_Table']['task_description'] = task_description
        self.temp_database[key]['User_Sponsor_Table']['train_file_path'] = train_file_path
        self.temp_database[key]['User_Sponsor_Table']['train_id_path'] = train_id_path
        self.temp_database[key]['User_Sponsor_Table']['train_data_path'] = train_data_path
        self.temp_database[key]['User_Sponsor_Table']['train_target_path'] = train_target_path
        self.temp_database[key]['User_Sponsor_Table']['test_file_path'] = test_file_path
        self.temp_database[key]['User_Sponsor_Table']['test_id_path'] = test_id_path
        self.temp_database[key]['User_Sponsor_Table']['test_data_path'] = test_data_path
        self.temp_database[key]['User_Sponsor_Table']['test_target_path'] = test_target_path

        return 
    
    def get_User_Sponsor_Table(self, user_id: str, task_id: str, test_indicator: str, test_id: str=None):

        key = None
        if test_indicator == 'train':
            key = (user_id, task_id, test_indicator)
        elif test_indicator == 'test':
            key = (user_id, test_id, test_indicator)

        user_id = self.temp_database[key]['User_Sponsor_Table']['user_id']
        task_id = self.temp_database[key]['User_Sponsor_Table']['task_id']
        test_indicator = self.temp_database[key]['User_Sponsor_Table']['test_indicator']
        task_mode = self.temp_database[key]['User_Sponsor_Table']['task_mode']
        model_name = self.temp_database[key]['User_Sponsor_Table']['model_name']
        metric_name = self.temp_database[key]['User_Sponsor_Table']['metric_name']
        test_id = self.temp_database[key]['User_Sponsor_Table']['test_id']
        task_name = self.temp_database[key]['User_Sponsor_Table']['task_name']
        task_description = self.temp_database[key]['User_Sponsor_Table']['task_description']
        train_file_path = self.temp_database[key]['User_Sponsor_Table']['train_file_path']
        train_id_path = self.temp_database[key]['User_Sponsor_Table']['train_id_path']
        train_data_path = self.temp_database[key]['User_Sponsor_Table']['train_data_path']
        train_target_path = self.temp_database[key]['User_Sponsor_Table']['train_target_path']
        test_file_path = self.temp_database[key]['User_Sponsor_Table']['test_file_path']
        test_id_path = self.temp_database[key]['User_Sponsor_Table']['test_id_path']
        test_data_path = self.temp_database[key]['User_Sponsor_Table']['test_data_path']
        test_target_path = self.temp_database[key]['User_Sponsor_Table']['test_target_path']

        return (user_id, task_id, test_indicator, task_mode, model_name, metric_name, test_id, task_name, task_description, train_file_path, train_id_path,
                train_data_path, train_target_path, test_file_path, test_id_path, test_data_path, test_target_path)

    def store_User_Assistor_Table(self, user_id: str, task_id: str, test_indicator: str, task_mode: str, model_name: str, metric_name: str, test_id: str=None, 
                                task_name: str=None, task_description: str=None, train_file_path: str=None, train_id_path: str=None, train_data_path: str=None, 
                                test_file_path: str=None, test_id_path: str=None, test_data_path: str=None):
        
        key = None
        if test_indicator == 'train':
            key = (user_id, task_id, test_indicator)
        elif test_indicator == 'test':
            key = (user_id, test_id, test_indicator)

        self.temp_database[key]['User_Sponsor_Table']['user_id'] = user_id
        self.temp_database[key]['User_Sponsor_Table']['task_id'] = task_id
        self.temp_database[key]['User_Sponsor_Table']['test_indicator'] = test_indicator
        self.temp_database[key]['User_Sponsor_Table']['task_mode'] = task_mode
        self.temp_database[key]['User_Sponsor_Table']['model_name'] = model_name
        self.temp_database[key]['User_Sponsor_Table']['metric_name'] = metric_name
        self.temp_database[key]['User_Sponsor_Table']['test_id'] = test_id
        self.temp_database[key]['User_Sponsor_Table']['task_name'] = task_name
        self.temp_database[key]['User_Sponsor_Table']['task_description'] = task_description
        self.temp_database[key]['User_Sponsor_Table']['train_file_path'] = train_file_path
        self.temp_database[key]['User_Sponsor_Table']['train_id_path'] = train_id_path
        self.temp_database[key]['User_Sponsor_Table']['train_data_path'] = train_data_path
        self.temp_database[key]['User_Sponsor_Table']['test_file_path'] = test_file_path
        self.temp_database[key]['User_Sponsor_Table']['test_id_path'] = test_id_path
        self.temp_database[key]['User_Sponsor_Table']['test_data_path'] = test_data_path
        
        return
    
    def get_User_Assistor_Table(self, user_id: str, task_id: str, test_indicator: str, test_id: str=None):

        key = None
        if test_indicator == 'train':
            key = (user_id, task_id, test_indicator)
        elif test_indicator == 'test':
            key = (user_id, test_id, test_indicator)

        user_id = self.temp_database[key]['User_Sponsor_Table']['user_id']
        task_id = self.temp_database[key]['User_Sponsor_Table']['task_id']
        test_indicator = self.temp_database[key]['User_Sponsor_Table']['test_indicator']
        task_mode = self.temp_database[key]['User_Sponsor_Table']['task_mode']
        model_name = self.temp_database[key]['User_Sponsor_Table']['model_name']
        metric_name = self.temp_database[key]['User_Sponsor_Table']['metric_name']
        test_id = self.temp_database[key]['User_Sponsor_Table']['test_id']
        task_name = self.temp_database[key]['User_Sponsor_Table']['task_name']
        task_description = self.temp_database[key]['User_Sponsor_Table']['task_description']
        train_file_path = self.temp_database[key]['User_Sponsor_Table']['train_file_path']
        train_id_path = self.temp_database[key]['User_Sponsor_Table']['train_id_path']
        train_data_path = self.temp_database[key]['User_Sponsor_Table']['train_data_path']
        test_file_path = self.temp_database[key]['User_Sponsor_Table']['test_file_path']
        test_id_path = self.temp_database[key]['User_Sponsor_Table']['test_id_path']
        test_data_path = self.temp_database[key]['User_Sponsor_Table']['test_data_path']

        return (user_id, task_id, test_indicator, task_mode, model_name, metric_name, test_id, task_name, task_description, train_file_path, train_id_path,
                train_data_path, test_file_path, test_id_path, test_data_path)


