R = float(input())
R = (1000 * R + 5) // 10
cnt = 1
while True:
    if R * cnt % 36000 == 0:
        print(cnt)
        break
    cnt += 1