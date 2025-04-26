import sys
input = sys.stdin.readline

while True:
    try:
        capacity = input().rstrip()
        n = int(capacity[2:])  # 분수 1/n의 분모
    except ValueError:
        break

    cnt = 1
    tmp = n

    # 2의 지수 처리
    e = 0
    while tmp % 2 == 0:
        tmp //= 2
        e += 1
    if e:
        cnt *= (2 * e + 1)

    # 홀수인 소인수 처리
    p = 3
    while p ** 2 <= tmp:
        if tmp % p == 0:
            e = 0
            while tmp % p == 0:
                tmp //= p
                e += 1
            cnt *= (2 * e + 1)
        p += 2

    # 남은 소인수가 있을 경우 추가 처리
    if tmp > 1:
        cnt *= 3  # 2 * 1 + 1

    print((cnt + 1) // 2)