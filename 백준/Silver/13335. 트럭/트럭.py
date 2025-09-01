import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0] * w)
total_weight = 0
time = 0


def step(q, w_in):
    # 매 초 다리 위의 트럭 무게를 연산하는 함수
    global total_weight, time
    q.appendleft(w_in)
    w_out = q.pop()
    total_weight += w_in
    total_weight -= w_out
    time += 1


while trucks:
    if total_weight + trucks[0] - bridge[-1] <= L:
        step(bridge, trucks.popleft())
    else:
        step(bridge, 0)

if any(bridge):
    # 트럭이 한 대라도 다리 위에 남아있을 경우
    while any(bridge):
        step(bridge, 0)

print(time)