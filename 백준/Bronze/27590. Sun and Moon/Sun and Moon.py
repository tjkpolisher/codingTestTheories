d_s, y_s = map(int, input().split())
d_m, y_m = map(int, input().split())

sun_year = y_s - d_s
moon_year = y_m - d_m

while sun_year != moon_year:
    if sun_year < moon_year:
        sun_year += y_s
    else:
        moon_year += y_m
print(sun_year)