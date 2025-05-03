CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    display_name TEXT
);

CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    start_time TEXT,
    end_time TEXT,
    duration REAL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
