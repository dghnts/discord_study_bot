SELECT *
FROM sessions
WHERE user_id = ?
ORDER BY start_time;
