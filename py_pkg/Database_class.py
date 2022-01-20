
class Database():
    __Database_instance = None

    def __init__(self):
        pass

    @classmethod
    def get_Database_instance(cls):
        if cls.__Database_instance == None:
            cls.__Database_instance = Database()

        return cls.__Database_instance

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

    
