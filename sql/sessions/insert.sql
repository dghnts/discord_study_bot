-- セッション情報の追加 --
--- durationはpythonで計算する ---
INSERT INTO sessions (start_time, end_time, user_id)
VALUES (?, NULL, ?);
