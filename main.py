import threading
import os

from init_db import init_database
from web.app import create_app
from bot import run_bot  # bot.py に run_bot 関数を定義


def run_web():
    app = create_app()
    port = int(os.getenv("PORT",5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Flaskを別スレッドで実行
    t = threading.Thread(target=run_web)
    t.start()

    init_database()
    run_bot()
