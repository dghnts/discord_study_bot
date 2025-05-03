from pathlib import Path

from utils.sql_loader import load_sql
from service.service_interface import ServiceInterface

class UserService(ServiceInterface):
    def __init__(self, db_path="data/sessions.db"):
        super().__init__(db_path)
        """SQLの読み込み"""
        self.user_sql = load_sql("users")

    '''新規ユーザーの追加'''
    def add_new_user(self, user_id: str, display_name: str):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(self.user_sql["insert"], (user_id, display_name))

    '''idでユーザー検索'''
    def find_by_id(self, user_id: str) -> tuple:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(self.user_sql["find_by_id"], (user_id,))
        return cursor.fetchone()

    """全ユーザーを取得"""
    def get_all_users(self) -> list:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(self.user_sql["select_all"])
        return cursor.fetchall()