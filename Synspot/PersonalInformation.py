import os

# from Database import Session, User_Default_Path, assign_value_to_user_default_path_instance

class PersonalInformation:
    __PersonalInformation_instance = None

    def __init__(self):
        self.__default_mode = None
        self.__user_id = None
        self.__root = os.path.abspath(os.path.dirname(__file__))
        self.__exe_position = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dist', 'run', 'run')
        
    @classmethod
    def get_PersonalInformation_instance(cls):
        if cls.__PersonalInformation_instance == None:
            cls.__PersonalInformation_instance = PersonalInformation()

        return cls.__PersonalInformation_instance

    @property
    def user_id(self):
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

    @user_id.setter
    def user_id(self, user_id: str):
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

    @property
    def default_mode(self):
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
            self.__default_mode = "auto"
        return self.__default_mode

    @default_mode.setter
    def default_mode(self, mode: str):
        """
        Change the default mode.

        Parameters:
         mode - String. Must in ["auto", "manual"]

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """
        
        if mode not in {'auto', 'manual'}:
            raise Exception("Sorry, default mode wrong")
        self.__default_mode = mode
        return

    @property
    def root(self):
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

    @root.setter
    def root(self, root: str):
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

    @property
    def exe_position(self):
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

    def logout(self):
        """
        Handle user logout by setting the __default_mode and __user_id to None

        Parameters:
            None

        Returns:
            None

        Raises:
            KeyError - raises an exception
        """
        try:
            self.__default_mode = None
            self.__user_id = None
        except:
            print('Logout procedure wrong')
