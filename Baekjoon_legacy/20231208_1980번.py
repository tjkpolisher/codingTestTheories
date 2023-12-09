# 1980: 햄버거 사랑
import sys

input = sys.stdin.readline
n, m, t = map(int, input().split())
max_hamburgers = 0 # 최대 햄버거 개수
min_cola_time = t # 콜라를 마시는 데 걸리는 최소 시간

if n > m:
    n, m = m, n
print("t // m =", t//m)
print("t // n =", t//n)

for i in range(t // m + 1): # 먹는 시간이 긴 햄버거를 먹는 경우의 수
    j = (t - m * i) // n # 남은 시간동안 먹는 시간이 짧은 햄버거를 먹는 경우의 수

    time = n * j + m * i # 먹는데 걸리는 시간
    hamburgers = i + j # 먹은 햄버거 개수
    cola_time = t - time # 콜라를 마시는 시간

    # 먹은 햄버거 개수가 이전 최대치보다 많거나, 같은 경우 콜라 마시는 시간이 더 적은 경우
    if hamburgers >= max_hamburgers or cola_time < min_cola_time:
        max_hamburgers = hamburgers
        min_cola_time = cola_time

print(max_hamburgers, min_cola_time)