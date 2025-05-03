from abc import ABC, abstractmethod

from repository.storage_interface import StorageInterface
from domain.users import User

class JsonStorageInterface(ABC,StorageInterface):
    @abstractmethod
    def _load(self):
        pass

    def _save(self):
        pass

    def start(self, user_id: str, display_name: str):
        pass

    def end(self, user_id: str, display_name: str):
        pass

    def get_user(self, user_id: str):
        pass


    def get_all_users(self):
        pass
