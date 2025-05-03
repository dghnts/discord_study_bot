DELETE FROM sessions WHERE user_id = ? AND end_time IS NULL;
