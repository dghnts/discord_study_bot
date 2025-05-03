SELECT end_time, user_id, duration FROM sessions
WHERE user_id = ? AND end_time IS NOT NULL
ORDER BY start_time;
