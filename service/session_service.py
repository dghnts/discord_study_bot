from domain.session import Session
from repository.session_repository import SessionRepository


class SessionService:

    def __init__(self, session_repo: SessionRepository):
        self.session_repo = session_repo

    def register(self, session: Session):
        """
        セッション情報をデータベースに追加する
        """
        session_data = session.to_db_tuple()
        self.session_repo.create(session_data)
