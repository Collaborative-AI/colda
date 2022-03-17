class Network():
    __Network_instance = None

    def __init__(self):
        self.__token = None
        # self.__baseURL = 'http://3.15.30.244'
        # self.__baseURL = 'http://localhost:5000'
        # self.__baseURL = 'http://127.0.0.1:5000'
        self.__baseURL = 'http://3.145.140.55'

    @classmethod
    def get_Network_instance(cls):
        if cls.__Network_instance == None:
            cls.__Network_instance = Network()

        return cls.__Network_instance

    @property
    def base_url(self):
        """
        Get base url that is the ipv4 address of AWS server and return base url

        :returns: base url, a string of server ipv4 address

        :exception OSError: Placeholder.
        """
        return self.__baseURL

    @property
    def token(self):
        """
        Return the token

        :returns: token - string.

        :exception OSError: Placeholder.
        """
        # print("zz", self.__token)
        return self.__token

    @token.setter
    def token(self, token: str):
        """
        Set token to new token

        :param token: string. Token sent by the server

        :returns: None

        :exception OSError: Placeholder.
        """
        self.__token = token
        # print("new_token", self.__token)
        return 

    def logout(self):
        """
        Handle user logout by setting the __token to None

        :returns: None

        :exception OSError: Placeholder.
        """
        try:
            self.__token = None
        except:
            print('Logout procedure wrong')
        