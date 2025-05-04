from domain.session import Session
from repository.session_repository import SessionRepository


class TimerService:
    def __init__(self, session_repo: SessionRepository):
        self.session_repo = session_repo

    def get_total_time_by_user(self, user_id: str) -> float:
        """ユーザーごとの累積作業時間（分）を返す"""
        raw_sessions = self.session_repo.get_by_user(user_id)
        sessions = [Session.from_dict(row) for row in raw_sessions]
        return sum(s.duration for s in sessions)

    def get_daily_time_by_user(self, user_id: str) -> float:
        """日ごとの作業時間を {日付: 分数} 形式で返す"""
        raw_sessions = self.session_repo.get_today_by_user(user_id)
        sessions = [Session.from_dict(row) for row in raw_sessions]

        return sum(s.duration for s in sessions)
