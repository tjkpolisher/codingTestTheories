from datetime import datetime
time_and_date = datetime.strptime(input(),
                                  "%B %d, %Y %H:%M")
year_start = datetime.strptime(f"{time_and_date.year} 01 01 00:00",
                               "%Y %m %d %H:%M")
diff = time_and_date - year_start
diff = diff.days * 24 * 3600 + diff.seconds
if time_and_date.year % 400 == 0 or (time_and_date.year % 4 == 0 and time_and_date.year % 100 != 0):
    answer = diff / 366 / 24 / 3600 * 100
else:
    answer = diff / 365 / 24 / 3600 * 100
print(answer)