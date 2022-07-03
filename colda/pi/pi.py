from __future__ import annotations

import os

from colda.pi.base import BasePI

from colda.utils.api import (
    del_instance,
    Constant
)

from colda._typing import Mode

from typeguard import typechecked


#@typechecked
class PI(BasePI):
    '''
    Store personal information

    Attributes
    ----------
    user_id
    default_mode
    root

    Methods
    -------
    logout
    '''

    __PI_instance = None

    def __init__(self):
        self.__default_mode = Constant.INITIAL_DEFAULT_MODE
        self.__user_id = None
        self.__data_storage_root = os.path.abspath(os.path.dirname(__file__))
        
    @classmethod
    def get_instance(cls) -> type[PI]:
        '''
        Singleton pattern. 
        Get instance of current class.

        Parameters
        ----------
        None

        Returns
        -------
        type[PI]
        '''
        if cls.__PI_instance == None:
            cls.__PI_instance = PI()

        return cls.__PI_instance

    @property
    def user_id(self) -> str:
        '''
        Get the user id.

        Parameters
        ----------
        None

        Returns
        -------
        str
        '''
        return self.__user_id

    @user_id.setter
    def user_id(
        self, user_id: str
    ) -> None:
        '''
        Set the user id.

        Parameters
        ----------
        user_id : str

        Returns
        -------
        bool
        '''
        self.__user_id = user_id
        return

    @property
    def default_mode(self) -> str:
        '''
        Get the default mode.
        default mode is set to 'auto' at first

        Parameters
        ----------
        None

        Returns
        -------
        str
        '''
        return self.__default_mode

    @default_mode.setter
    def default_mode(
        self, default_mode: Mode
    ) -> None:
        '''
        Change the default mode.

        Parameters
        ----------
        default_mode : str
            default_mode decides the execution way when assistor
            receives the collaboration request

        Returns
        -------
        None
        '''
        self.__default_mode = default_mode
        return

    @property
    def data_storage_root(self) -> str:
        '''
        Get the root path of data storage.
        Default data_storage_root is the path of 
        current file.

        Parameters
        ----------
        None

        Returns
        -------
        str
        '''
        return self.__data_storage_root

    @data_storage_root.setter
    def data_storage_root(
        self, data_storage_root: str
    ) -> None:
        '''
        Set the data_storage_root path

        Parameters
        ----------
        None

        Returns
        -------
        str
        '''
        self.__data_storage_root = data_storage_root
        return

    @classmethod
    def logout(cls) -> None:
        '''
        Handle user logout by deleting instance

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        del_instance(
            objectInstance=cls.__PI_instance
        )
            
        return
    
    @classmethod
    def delete(cls):
        cls.__PI_instance = None