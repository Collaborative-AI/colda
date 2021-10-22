
class PersonalInformation:
    __PersonalInformation_instance = None

    def __init__(self):
        self.__default_mode = None
        self.__user_id = None

    @classmethod
    def get_PersonalInformation_instance(cls):
        if cls.__PersonalInformation_instance == None:
            cls.__PersonalInformation_instance = PersonalInformation()

        return cls.__PersonalInformation_instance

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
            self.__default_mode = "passive"
        return self.__default_mode


    def set_default_mode(self, mode: str):
        """
        Change the default mode.

        Parameters:
         mode - String. Must in ["passive", "active", "auto"]

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """

        self.__default_mode = mode
        return