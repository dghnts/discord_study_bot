from init_db import init_database
from bot import run_bot  # bot.py に run_bot 関数を定義

if __name__ == "__main__":
    init_database()
    run_bot()
