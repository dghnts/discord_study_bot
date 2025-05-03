from repository.storage import StorageInterface

class TimerService:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def start_session(self, user_id: str, display_name: str):
        """セッション開始"""
        self.storage.start_session(user_id, display_name)

    def end_session(self, user_id: str, display_name: str):
        """セッション終了"""
        duration, total_minutes = self.storage.end_session(user_id, display_name)
        return duration, total_minutes

    def get_user_info(self, user_id: str):
        """特定ユーザー情報の取得"""
        return self.storage.get_user(user_id)

    def get_all_users(self):
        """全ユーザー情報の取得"""
        return self.storage.get_all_users()
