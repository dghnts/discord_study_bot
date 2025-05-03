from controller.events import login,session_events
from service.session_service import SessionService

""",session_service: SessionService, tracked_vc_id: int"""
def register_all_events(bot, session_service: SessionService, tracked_vc_id: int ):
    login.login_event(bot)
    session_events.session_event(bot, tracked_vc_id)
