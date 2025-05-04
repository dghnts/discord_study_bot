import sqlite3

from repository.base_repository import BaseRepository
from utils.sql_loader import load_sql


class SessionRepository(BaseRepository):

    def __init__(self):
        super().__init__()
        # SQLの読み込み
        self.session_sql = load_sql("sessions")

    def create(self, session_data: tuple):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(self.session_sql["insert"], session_data)
            conn.commit()

    def get_by_user(self, user_id: str) -> list[dict]:
        """ユーザーIDに紐づくすべてのセッションを辞書形式で返す"""
        with self._connect() as conn:
            conn.row_factory = sqlite3.Row  # Row型で辞書のように扱う
            cursor = conn.cursor()
            cursor.execute(self.session_sql["select_by_user_id"], (user_id,))
            rows = cursor.fetchall()
        return [dict(row) for row in rows]

    def get_today_by_user(self, user_id: str) -> list[dict]:
        """ユーザーの今日のセッションを辞書のリストとして取得する"""
        with self._connect() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(self.session_sql["select_today_by_user"], (user_id,))
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
