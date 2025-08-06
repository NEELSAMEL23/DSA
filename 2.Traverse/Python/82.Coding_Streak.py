def coding_streak(n, logs):
    max_coding_minutes = 0  # X
    max_coding_days_streak = 0  # Y
    current_coding_days_streak = 0

    for log in logs:
        # Find max consecutive 'C' in the current day's log
        current_streak = 0
        max_streak_day = 0
        for ch in log:
            if ch == 'C':
                current_streak += 1
                max_streak_day = max(max_streak_day, current_streak)
            else:
                current_streak = 0
        max_coding_minutes = max(max_coding_minutes, max_streak_day)

        # Check if the whole day was coding only
        if all(ch == 'C' for ch in log):
            current_coding_days_streak += 1
            max_coding_days_streak = max(max_coding_days_streak, current_coding_days_streak)
        else:
            current_coding_days_streak = 0

    print(f"{max_coding_minutes} {max_coding_days_streak}")

n = 4
logs = [
    "SSSSSCCCCCCCCCCCCE",
    "CCCCCCCCCCCCCCCCC",
    "SSSSSCCCCCCCCCCCCE",
    "FFFFFFFFCCCCCCCCCE"
]
coding_streak(n, logs)