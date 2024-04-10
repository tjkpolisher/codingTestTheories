import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lamps = list(map(int, input().split()))

if M == 1:
    height = max(lamps[0], N - lamps[0])
else:
    height = lamps[0]
    for i in range(M):
        # 마지막 가로등일 때
        if i == M - 1:
            tmp = N - lamps[-1]
        # 나머지 가로등
        else:
            distance = lamps[i + 1] - lamps[i]
            # 가로등 사이의 거리가 홀수일 경우, 가로등이 1만큼 더 높아야 모든 거리를 비출 수 있음
            # 짝수일 경우는 그대로 가져가도 무방
            tmp = distance // 2 + 1 if distance % 2 == 1 else distance // 2

        height = max(height, tmp)

print(height)