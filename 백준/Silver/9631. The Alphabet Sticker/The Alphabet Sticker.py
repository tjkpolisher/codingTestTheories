import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

T = int(input())
for _ in range(T):
    sticker = input().rstrip()
    result = 1
    n = len(sticker)
    i = 0

    while i < n:
        if sticker[i] == '?':
            j = i
            while j < n and sticker[j] == '?':
                j += 1

            # j는 이제 물음표가 아닌 위치 또는 문자열 끝을 가리킴
            left = sticker[i - 1] if i > 0 else None
            right = sticker[j] if j < n else None

            if left and right:
                if left != right:
                    result *= (j - i + 1)
                    result %= MOD

            i = j
        else:
            i += 1

    print(result % MOD)