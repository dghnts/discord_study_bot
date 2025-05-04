from datetime import datetime
from pathlib import Path

from service.service_interface import ServiceInterface
from utils.sql_loader import load_sql

SQL_DIR = Path("")

'''
    実装する処理
    新規セッションの作成
    セッションの終了
'''
class SessionService(ServiceInterface):

    def __init__(self, db_path="data/sessions.db"):
        super().__init__(db_path)
        """SQLの読み込み"""
        self.session_sql = load_sql("sessions")


    def add_new_session(self, session_data: tuple):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(self.session_sql["insert"], session_data)
            conn.commit()


    """終了していないsessionを取得"""
    def get_current_session(self, user_id: str) -> tuple:
        with self._connect() as conn:
            cursor = conn.cursor()

            cursor.execute(self.session_sql["select_current_session"], (user_id,))

        return cursor.fetchone()

    """セッション情報を更新する（終了時刻の追加）"""
    def add_end_time(self, session: tuple):
        now = datetime.now() # 現在時刻

        with self._connect() as conn:
            cursor = conn.cursor()

            session_id, start_time = session[0:2]
            start_dt = datetime.fromisoformat(start_time)
            duration = (now - start_dt).total_seconds() / 60

            cursor.execute(self.session_sql["update"],
                           (now.isoformat(), duration, session_id))

            conn.commit()

        return duration