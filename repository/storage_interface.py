from abc import ABC, abstractmethod
from domain.user import User

class StorageInterface(ABC):
    @abstractmethod
    def start_session(self, user_id: str, display_name: str):
        """作業開始時に呼び出す処理"""
        pass

    @abstractmethod
    def end_session(self, user_id: str, display_name: str) -> tuple[float, float] | tuple[None, None]:
        """作業終了時に呼び出す処理。戻り値は (今回の時間, 累積時間)"""
        pass

    @abstractmethod
    def get_user(self, user_id: str) -> User | None:
        """ユーザー情報の取得"""
        pass

    @abstractmethod
    def get_all_users(self) -> list[User]:
        """全ユーザーのリスト取得"""
        pass
