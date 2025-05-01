from domain.basemodel import BaseModel
from domain.session import Session

class User(BaseModel):
    def __init__(self, user_id: str, display_name: str):
        self.user_id = user_id
        self.display_name = display_name
        self.sessions = []  # List[Session]

    def add_session(self, session: Session):
        """ユーザーに新しいセッションを追加する"""
        self.sessions.append(session)

    @property
    def total_minutes(self) -> float:
        """このユーザーの累積作業時間を取得する（分単位）"""
        return round(sum(session.duration for session in self.sessions), 1)

    def to_dict(self) -> dict:
        """Userを辞書に変換する"""
        return {
            "display_name": self.display_name,
            "total_minutes": self.total_minutes,
            "sessions": [session.to_dict() for session in self.sessions]
        }

    @classmethod
    def from_dict(cls, user_id: str, data: dict):
        """辞書からUserを復元する"""
        user = cls(user_id, data["display_name"])
        for session_data in data.get("sessions", []):
            user.add_session(Session.from_dict(session_data))
        return user

    def __repr__(self):
        return f"<User id={self.user_id} name={self.display_name} sessions={len(self.sessions)} total_minutes={self.total_minutes:.1f}>"
