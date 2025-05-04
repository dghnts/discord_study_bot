from utils.sql_loader import load_sql
import sqlite3
import os
from config import DB_PATH

def init_database():
    # ディレクトリがなければ作成
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    # DBに接続
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 各テーブルのSQLをロードしてCREATE TABLE実行
    user_sql = load_sql("users")
    session_sql = load_sql("sessions")

    cursor.execute(user_sql["create"])
    cursor.execute(session_sql["create"])

    conn.commit()
    conn.close()
    print("✅ データベースの初期化が完了しました。")

if __name__ == "__main__":
    init_database()
