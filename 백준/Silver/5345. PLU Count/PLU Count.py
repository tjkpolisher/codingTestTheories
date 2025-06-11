import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip().lower()
    cnt = 0
    i = 0

    while i < len(s):
        if s[i] == 'p':
            # 'p' 발견 후, 다음 'l' 탐색
            j = i + 1
            while j < len(s) and s[j] != 'l':
                j += 1
            if j == len(s):
                break
            # 'l' 발견 후, 다음 'u' 탐색
            k = j + 1
            while k < len(s) and s[k] != 'u':
                k += 1
            if k == len(s):
                break

            cnt += 1
            i = k + 1
        else:
            i += 1

    print(cnt)