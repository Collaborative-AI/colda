from __future__ import annotations

from abc import ABC, abstractmethod

class AbstractLog:

    @abstractmethod
    def store_log(self, *args):
        pass
    
    @abstractmethod
    def get_log(self, *args):
        pass
    
    @abstractmethod
    def get_all_logs(self, *args):
        pass

    @abstractmethod
    def log_serialization(self):
        pass

    