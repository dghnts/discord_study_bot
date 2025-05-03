SELECT start_time, end_time FROM sessions
WHERE user_id = ? AND end_time IS NOT NULL
ORDER BY start_time;
