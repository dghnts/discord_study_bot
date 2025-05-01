from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        """インスタンスを辞書に変換する"""
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict):
        """辞書からインスタンスを復元する"""
        pass
