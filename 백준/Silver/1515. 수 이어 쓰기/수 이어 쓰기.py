import sys
input = sys.stdin.readline

num = input().rstrip()

ans = 0
while True:
    ans += 1
    ans_str = str(ans)
    while len(num) > 0 and len(ans_str) > 0:
        if num[0] == ans_str[0]:
            num = num[1:]
        ans_str = ans_str[1:]
    if not num:
        print(ans)
        break