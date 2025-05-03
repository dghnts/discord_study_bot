SELECT id, start_time, end_time, duration FROM sessions
WHERE user_id = ?
ORDER BY start_time DESC LIMIT 1;
