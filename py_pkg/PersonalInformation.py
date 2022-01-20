import os
from Database import Session, User_Default_Path, assign_value_to_user_default_path_instance
class PersonalInformation:
    __PersonalInformation_instance = None

    def __init__(self):
        self.__default_mode = None
        self.__user_id = None
        self.__root = os.path.abspath(os.path.dirname(__file__))
        print(self.__root)
        self.__exe_position = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dist', 'run', 'run')
        print(self.__exe_position)

    @classmethod
    def get_PersonalInformation_instance(cls):
        if cls.__PersonalInformation_instance == None:
            cls.__PersonalInformation_instance = PersonalInformation()

        return cls.__PersonalInformation_instance

    def get_default_path(self):
        """
        get the user id of current user. The user id is set to None at first.

        Parameters:
         None

        Returns:
         The user id of current user.

        Raises:
         KeyError - raises an exception
        """
        user_id = self.get_user_id()
        session = Session()
        query = session.query(User_Default_Path).filter_by(user_id=user_id).first()
        default_train_file_path = query.default_train_file_path
        default_train_id_column = query.default_train_id_column
        default_train_data_column = query.default_train_data_column

        return default_train_file_path, default_train_id_column, default_train_data_column

    def set_default_path(self, default_train_file_path: str, default_train_id_column: str, default_train_data_column: str):
        """
        Change the default_path.

        Parameters:
         None

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        user_id = self.get_user_id()
        session = Session()
        user_default_path = User_Default_Path()
        user_default_path = assign_value_to_user_default_path_instance(user_default_path, user_id, default_train_file_path,
                                                                      default_train_id_column, default_train_data_column)
        session.add(user_default_path)
        session.commit()
        return

    def get_user_id(self):
        """
        get the user id of current user. The user id is set to None at first.

        Parameters:
         None

        Returns:
         The user id of current user.

        Raises:
         KeyError - raises an exception
        """

        return self.__user_id

    def set_user_id(self, user_id: str):
        """
        Change the user_id.

        Parameters:
         user_id - String.

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        self.__user_id = user_id
        return

    def get_default_mode(self):
        """
        get the default mode set by user from DB. The default mode is set to active at first.

        Parameters:
         None

        Returns:
         The default mode set by user.

        Raises:
         KeyError - raises an exception
        """

        if self.__default_mode == None:
            # get message from database
            self.__default_mode = "manual"
        return self.__default_mode


    def set_default_mode(self, mode: str):
        """
        Change the default mode.

        Parameters:
         mode - String. Must in ["auto", "manual"]

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        self.__default_mode = mode
        return

    def get_root(self):
        """
        Get the root path of intermediate data storage

        Parameters:
         None

        Returns:
         The root path of intermediate data storage.

        Raises:
         KeyError - raises an exception
        """

        return self.__root


    def set_root(self, root: str):
        """
        Set the root path of intermediate data storage to new root

        Parameters:
         root - String. Must be valid

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        self.__root = root
        return

    def get_exe_position(self):
        """
        Get the path of the Algorithm entry point

        Parameters:
         None

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        return self.__exe_position


# c = PersonalInformation.get_PersonalInformation_instance()