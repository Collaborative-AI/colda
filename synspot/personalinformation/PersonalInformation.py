import os

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

        :returns: The user id of current user.

        :exception OSError: Placeholder.
        """

        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """
        Change the user_id.

        :param user_id: String.

        :returns: None

        :exception OSError: Placeholder.
        """

        self.__user_id = user_id
        return

    @property
    def default_mode(self):
        """
        get the default mode set by user from DB. The default mode is set to active at first.

        :returns: The default mode set by user.

        :exception OSError: Placeholder.
        """

        if self.__default_mode == None:
            # get message from database
            self.__default_mode = "auto"
        return self.__default_mode

    @default_mode.setter
    def default_mode(self, mode: str):
        """
        Change the default mode.

        :param mode: String. Must in ["auto", "manual"]

        :returns: None

        :exception OSError: Placeholder.
        """
        
        if mode not in {'auto', 'manual'}:
            raise Exception("Sorry, default mode wrong")
        self.__default_mode = mode
        return

    @property
    def root(self):
        """
        Get the root path of intermediate data storage

        :returns: The root path of intermediate data storage.

        :exception OSError: Placeholder.
        """

        return self.__root

    @root.setter
    def root(self, root: str):
        """
        Set the root path of intermediate data storage to new root

        :param root: String. Must be valid

        :returns: None

        :exception OSError: Placeholder.
        """

        self.__root = root
        return

    @property
    def exe_position(self):
        """
        Get the path of the Algorithm entry point

        :returns: None

        :exception OSError: Placeholder.
        """

        return self.__exe_position

    def logout(self):
        """
        Handle user logout by setting the __default_mode and __user_id to None

        :returns: None

        :exception OSError: Placeholder.
        """
        try:
            self.__default_mode = None
            self.__user_id = None
        except:
            print('Logout procedure wrong')
