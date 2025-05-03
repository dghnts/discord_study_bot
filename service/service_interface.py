import sqlite3
class ServiceInterface():

    def __init__(self, db_path="data/sessions.db"):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)