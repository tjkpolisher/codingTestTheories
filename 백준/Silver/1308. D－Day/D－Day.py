from datetime import datetime
a, b, c = map(int, input().split())
a = f"{a:04d}"
today = datetime.strptime(f"{a} {b} {c}", "%Y %m %d")
a, b, c = map(int, input().split())
a = f"{a:4d}"
dday = datetime.strptime(f"{a} {b} {c}", "%Y %m %d")

if dday.year - today.year > 1000:
    print("gg")
elif dday.year - today.year == 1000 and (dday.month, dday.day) >= (today.month, today.day):
    print("gg")
else:
    x = dday - today
    print(f"D-{x.days}")