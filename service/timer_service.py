from datetime import datetime

from repository.storage_interface import StorageInterface


class TimerService:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def total_minutes(self, date=None, user_id=None,session_sql=None):
        sessions = []

        if not date:
            """日時の指定がないとき"""
            """ユーザーのセッション情報をすべて取得する"""
            sessions = session_sql["select_user_sessions"]
        else:
            """日時の指定があるとき"""
            sessions = [
                session for session \
                in session_sql["select_user_sessions_by_date"] \
                if session.end_time == date
            ]

        ret = 0

        for session in sessions:
            ret += session.duration

        return ret

    def get_today_minutes(self, user_id: str) -> float:
        today = datetime.now().date()
        user = self.storage.get_user(user_id)

        print(user)
        return 0.0
