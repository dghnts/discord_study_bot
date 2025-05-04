SELECT *
FROM sessions
WHERE user_id = ?
  AND DATE(start_time) = DATE('now', 'localtime');
