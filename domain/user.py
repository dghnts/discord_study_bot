from domain.base_model import BaseModel


class User(BaseModel):
    def __init__(self, user_id: str, display_name: str):
        self.user_id = user_id
        self.display_name = display_name

    def to_dict(self) -> dict:
        """Userを辞書に変換する"""
        return {
            "user_id": self.user_id,
            "display_name": self.display_name
        }

    @classmethod
    def from_dict(cls, data: dict):
        """辞書からUserを復元する"""
        return cls(data["user_id"], data["display_name"])

    def __repr__(self):
        return f"<User id={self.user_id} name={self.display_name}>"
