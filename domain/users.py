from domain.basemodel import BaseModel
from utils.sql_loader import load_sql

class User(BaseModel):
    def __init__(self, user_id: str, display_name: str):
        self.user_id = user_id
        self.display_name = display_name

    def to_dict(self) -> dict:
        """Userを辞書に変換する"""
        return {
            "display_name": self.display_name,
            "sessions": [session.to_dict() for session in self.sessions]
        }

    @classmethod
    def from_dict(cls, user_id: str, data: dict):
        """辞書からUserを復元する"""
        user = cls(user_id, data["display_name"])

        return user

    def __repr__(self):
        return f"<User id={self.user_id} name={self.display_name}>"
