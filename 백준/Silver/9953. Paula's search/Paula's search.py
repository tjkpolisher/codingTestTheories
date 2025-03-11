import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break

    current = 50  # 시작 위치는 항상 50번 가게
    cnt = 0  # 파울라가 맞는 옷을 찾을 때까지 방문한 가게의 수
    odd_start, odd_end = 1, 99
    even_start, even_end = 2, 100

    while current != N:
        cnt += 1

        # 길 반대편으로 이동해야 할 경우
        if N % 2 != current % 2:
            if current % 2 == 0:  # 짝수에서 홀수로
                current = (odd_start + odd_end) // 2
                if current % 2 == 0:
                    current -= 1
            else:  # 홀수에서 짝수로
                current = (even_start + even_end) // 2
                if current % 2 == 1:
                    current -= 1
            continue

        # 같은 쪽에서의 이동
        if current % 2 == 0:  # 짝수 쪽 길
            if N < current:
                even_end = current - 2
            else:
                even_start = current + 2
            current = (even_start + even_end) // 2
            if current % 2 == 1:
                current -= 1
        else:  # 홀수 쪽 길
            if N < current:
                odd_end = current - 2
            else:
                odd_start = current + 2
            current = (odd_start + odd_end) // 2
            if current % 2 == 0:
                current -= 1

    print(cnt + 1)