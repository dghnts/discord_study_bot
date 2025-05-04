from flask import jsonify
from repository.session_repository import SessionRepository
from service.timer_service import TimerService

def register_routes(app):
    @app.route("/ping")
    def ping():
        return "pong", 200

    @app.route("/users/<user_id>/total_minutes")
    def total_minutes(user_id):
        session_repo = SessionRepository()
        timer_service = TimerService(session_repo)
        total = timer_service.get_total_time_by_user(user_id)
        return jsonify({"user_id": user_id, "total_minutes": total or 0})
