
class Network():
    __Network_instance = None

    def __init__(self):
        self.__token = None
        self.__baseURL = 'http://3.15.30.244'
        # self.__baseURL = 'http://localhost:5000'

    @classmethod
    def get_Network_instance(cls):
        if cls.__Network_instance == None:
            cls.__Network_instance = Network()

        return cls.__Network_instance

    def get_base_url(self):
        """
        Get base url that is the ipv4 address of AWS server and return base url

        Parameters:
         None

        Returns:
         base url, a string of server ipv4 address

        Raises:
         KeyError - raises an exception
        """
        return self.__baseURL

    def set_token(self, token: str):
        """
        Set token to new token

        Parameters:
         token - string. Token sent by the server

        Returns:
         None

        Raises:
         KeyError - raises an exception
        """
        self.__token = token
        print("new_token", self.__token)

    def get_token(self):
        """
        Return the token

        Parameters:
         None

        Returns:
         token - string.

        Raises:
         KeyError - raises an exception
        """
        print("zz", self.__token)
        return self.__token
