from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseModel(ABC):
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """インスタンスを辞書に変換する"""
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]):
        """辞書からインスタンスを復元する"""
        pass
