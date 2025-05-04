from flask import Flask, jsonify

from bot import timer_service
from service.timer_service import TimerService

def create_app()
    app = Flask(__name__)
    timer_service = TimerService()

    @app.route("users/<user_id>/total_minutes")
    def total_minutes(user_id):
        total = timer_service.get_total_time_by_user(user_id)
        return jsonify({"user_id": user_id, "total_minutes": total or 0})

    return app