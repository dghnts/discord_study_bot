CREATE TABLE IF NOT EXISTS sessions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_time TEXT,
    end_time TEXT,
    user_id TEXT,
    duration REAL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);