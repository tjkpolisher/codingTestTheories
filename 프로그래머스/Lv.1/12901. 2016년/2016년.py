def solution(a, b):
    from datetime import datetime
    now = datetime.strptime(f"2016-{a:02d}-{b:2d}", "%Y-%m-%d")
    weekday = now.weekday()
    answer = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"][weekday]
    return answer