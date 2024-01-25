from datetime import datetime
x, y = input().split()
now = datetime.strptime('-'.join(('2007', x, y)), '%Y-%m-%d')
weekday = now.weekday()
weekday_dict = {0: "MON", 1: "TUE", 2: "WED",
                3: "THU", 4: "FRI", 5: "SAT",
                6: "SUN"}
print(weekday_dict[weekday])