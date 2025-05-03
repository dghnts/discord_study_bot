import sqlite3
from repository.storage_interface import StorageInterface
from domain.user import User
from domain.session import Session
from datetime import datetime
from pathlib import Path

SQL_DIR = Path("sql")

def _load_sql(name: str) -> str:
    return (SQL_DIR / f"{name}.sql").read_text(encoding="utf-8")

class SqliteStorage(StorageInterface):
    def __init__(self, db_path="data/sessions.db"):
        self.db_path = db_path
        self._initialize_database()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _initialize_database(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.executescript(_load_sql("create_tables"))
            conn.commit()

    def start_session(self, user_id: str, display_name: str):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(_load_sql("insert_user_if_not_exists"), (user_id, display_name))
            cursor.execute("DELETE FROM sessions WHERE user_id = ? AND end_time IS NULL", (user_id,))
            cursor.execute(_load_sql("insert_session_start"), (user_id, datetime.now().isoformat()))
            conn.commit()

    def end_session(self, user_id: str, display_name: str):
        now = datetime.now()
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, start_time FROM sessions
                WHERE user_id = ? AND end_time IS NULL
                ORDER BY start_time DESC LIMIT 1
            """, (user_id,))
            row = cursor.fetchone()
            if not row:
                return None, None

            session_id, start_time = row
            start_dt = datetime.fromisoformat(start_time)
            duration = (now - start_dt).total_seconds() / 60

            cursor.execute(_load_sql("update_session_end"), (now.isoformat(), duration, session_id))

            cursor.execute("SELECT SUM(duration) FROM sessions WHERE user_id = ?", (user_id,))
            total_minutes = cursor.fetchone()[0] or 0.0

            conn.commit()
            return duration, total_minutes

    def get_user(self, user_id: str) -> User | None:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(_load_sql("select_user"), (user_id,))
            row = cursor.fetchone()
            if not row:
                return None
            display_name = row[0]

            cursor.execute(_load_sql("select_user_sessions"), (user_id,))
            sessions = [
                Session(datetime.fromisoformat(s), datetime.fromisoformat(e))
                for s, e in cursor.fetchall()
            ]
            return User(user_id, display_name)

    def get_all_users(self) -> list[User]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(_load_sql("select_all_users"))
            users = []
            for user_id, display_name in cursor.fetchall():
                cursor.execute(_load_sql("select_user_sessions"), (user_id,))
                sessions = [
                    Session(datetime.fromisoformat(s), datetime.fromisoformat(e))
                    for s, e in cursor.fetchall()
                ]
                users.append(User(user_id, display_name, sessions))
            return users
