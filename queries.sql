use final_project;

-- 1. Avg messages/day for every year and every month

-- MONTH

SELECT
    DATE_FORMAT(date, '%Y-%m') AS month,
    COUNT(*) / COUNT(DISTINCT date) AS avg_messages_per_day
FROM
    emsemotions
GROUP BY
    month;
    
-- YEAR

SELECT
    DATE_FORMAT(date, '%Y') AS year,
    ROUND(COUNT(*) / COUNT(DISTINCT date) AS avg_messages_per_day,2)
FROM
    emsemotions
GROUP BY
    year;

-- 2. Avarage message / emotion

SELECT
    max_emotion_day,
    ROUND(COUNT(*) / COUNT(DISTINCT date), 2) AS avg_messages_per_day
FROM
    pdef
GROUP BY
    max_emotion_day
ORDER BY avg_messages_per_day DESC;

-- 3. Top 5 daily emotions sorted by count

WITH ranked_emotions AS (
    SELECT
        date,
        emotions_names,
        COUNT(*) as emotion_count,
        RANK() OVER (PARTITION BY date ORDER BY COUNT(*) DESC) as emotion_rank
    FROM
        emsemotions
    GROUP BY
        date, emotions_names
)
SELECT
    emotions_names,
    SUM(emotion_count) as total_count
FROM
    ranked_emotions
WHERE
    emotion_rank <= 5 and emotions_names != "assertivity"
GROUP BY emotions_names
ORDER BY total_count DESC;

-- 4. Days of week count emotions when not happiness. Día maldito? Weekends weekdays

WITH ranked_emotions AS (
    SELECT
        day_of_week,
        max_emotion,
        end_day,
        COUNT(*) as emotion_count,
        RANK() OVER (PARTITION BY day_of_week, end_day ORDER BY COUNT(*) DESC) as emotion_rank
    FROM
        daylyemotions
    GROUP BY
        day_of_week, max_emotion, end_day
)
SELECT
    day_of_week,
    end_day,
    max_emotion,
    emotion_count
FROM
    ranked_emotions
WHERE
    emotion_rank = 2  
ORDER BY
    CASE
        WHEN day_of_week = 'Monday' THEN 1
        WHEN day_of_week = 'Tuesday' THEN 2
        WHEN day_of_week = 'Wednesday' THEN 3
        WHEN day_of_week = 'Thursday' THEN 4
        WHEN day_of_week = 'Friday' THEN 5
        WHEN day_of_week = 'Saturday' THEN 6
        WHEN day_of_week = 'Sunday' THEN 7
    END;

-- 5. Time range, morning, afternoon, night avg messages

SELECT
    CASE
        WHEN TIME_FORMAT(time, '%H:%i') BETWEEN '07:00' AND '14:00' THEN 'morning'
        WHEN TIME_FORMAT(time, '%H:%i') BETWEEN '14:00' AND '20:00' THEN 'afternoon'
        WHEN TIME_FORMAT(time, '%H:%i') >= '20:00' OR TIME_FORMAT(time, '%H:%i') < '02:00' THEN 'night'
    END AS time_range,
    COUNT(*) AS count_messages
FROM
    emsemotions
GROUP BY
    time_range
ORDER BY 
	count_messages desc
LIMIT 3;






