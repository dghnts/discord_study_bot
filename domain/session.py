from datetime import datetime

from domain.base_model import BaseModel


class Session(BaseModel):
    def __init__(self, data: dict) -> None:
        self.start_time = datetime.fromisoformat(data["start_time"])
        self.end_time = datetime.fromisoformat(data["end_time"])
        self.user_id = data["user_id"]

    @property
    def duration(self) -> float:
        return (self.end_time - self.start_time).total_seconds() / 60  # 分単位

    def to_dict(self) -> dict:
        return {
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "user_id": self.user_id,
            "duration": round(self.duration, 1)
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data)

    def to_db_tuple(self) -> tuple:
        return self.user_id, self.start_time.isoformat(), self.end_time.isoformat(), self.duration

    def __repr__(self):
        return f"<Session start_time={self.start_time} end_time={self.end_time} duration={self.duration:.1f}min>"
