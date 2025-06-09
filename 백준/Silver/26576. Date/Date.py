import sys
input = sys.stdin.readline

n = int(input())
month_dict = {"January": 1, "February": 2, "March": 3, "April": 4,
              "May": 5, "June": 6, "July": 7, "August": 8,
              "September": 9, "October": 10, "November": 11, "December": 12}


def transform(string):
    month, day, year = string.split()
    ans = []
    day = day[:-1]  # 쉼표 제거

    # 월 처리
    if month not in month_dict:
        return "Invalid"
    else:
        month = month_dict[month]
        ans.append(str(month).zfill(2))

    # 일 처리
    if int(day) < 1 or int(day) > 31:
        return "Invalid"
    else:
        day = day.zfill(2)
        ans.append(day)

    # 연도 처리
    if len(year) >= 2:
        ans.append(year[-2:])
    else:
        ans.append(year.zfill(2))
    return '/'.join(ans)


for _ in range(n):
    string = input().rstrip()
    print(transform(string))