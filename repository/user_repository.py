from repository.repository_interface import BaseRepository
from utils.sql_loader import load_sql


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        """SQLの読み込み"""
        self.user_sql = load_sql("users")

    """新規ユーザーの追加"""

    def create(self, user_id: str, display_name: str):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(self.user_sql["insert"], (user_id, display_name))

    """idでユーザー検索"""

    def get_by_id(self, user_id: str) -> tuple | None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(self.user_sql["find_by_id"], (user_id,))
        return cursor.fetchone()

    """全ユーザーを取得"""

    def get_all(self) -> list[tuple]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(self.user_sql["select_all"])
        return cursor.fetchall()
