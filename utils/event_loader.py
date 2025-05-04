from controller.events.login import login_event
from controller.events.session_events import session_event
from repository.session_repository import SessionRepository
from repository.user_repository import UserRepository

""",session_service: SessionService, tracked_vc_id: int"""


def register_all_events(bot, session_repo: SessionRepository, user_repo: UserRepository, tracked_vc_id: int):
    login_event(bot)
    session_event(bot, session_repo, user_repo, tracked_vc_id)
