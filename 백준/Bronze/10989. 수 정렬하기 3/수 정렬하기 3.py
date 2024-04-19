import sys
input = sys.stdin.readline

N = int(input())
cnt = [0] * 10001  # 각 수의 등장 횟수를 저장

# 등장하는 수마다 등장 횟수 증가
for _ in range(N):
    num = int(input())
    cnt[num] += 1

for i in range(10001):
    if cnt[i]:
        for j in range(cnt[i]):
            print(i)