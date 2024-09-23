import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s, p = input().rstrip().split()
    ls = len(s)
    lp = len(p)
    cnt = 0  # 타이핑 시간
    i = 0  # 인덱스
    while i < ls:
        string = s[i:i + lp]
        if string == p:
            i += lp
        else:
            i += 1
        cnt += 1
    print(cnt)