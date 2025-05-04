import sqlite3
from config import DB_PATH

class BaseRepository:

    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)
