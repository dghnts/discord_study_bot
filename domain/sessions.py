from datetime import datetime
from domain.basemodel import BaseModel

class Session(BaseModel):
    def __init__(self, start: datetime, end: datetime, user_id: str) -> None:
        self.start = start
        self.end = end
        self.user_id = user_id
        self.duration = (self.end - self.start).total_seconds() / 60  # 分単位

    def to_dict(self) -> dict:
        return {
            "start": self.start.isoformat(),
            "end": self.end.isoformat(),
            "duration": round(self.duration, 1)
        }

    @classmethod
    def from_dict(cls, user_id: str, data: dict):
        start = datetime.fromisoformat(data["start"])
        end = datetime.fromisoformat(data["end"])
        return cls(start, end, user_id)

    def __repr__(self):
        return f"<Session start={self.start} end={self.end} duration={self.duration:.1f}min>"
