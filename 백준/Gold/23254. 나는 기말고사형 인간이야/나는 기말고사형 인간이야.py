from heapq import heappush, heappop

N, M = map(int, input().split())  # 시험까지 남은 일수, 시험 볼 과목의 개수
a_list = list(map(int, input().split()))  # 기본 점수
b_list = list(map(int, input().split()))  # 공부할 때마다 오르는 점수

time = 0  # 총 공부 시간
heap = []  # 최대 힙
ans = 0  # 정답

for i in range(M):
    heappush(heap, (-b_list[i], a_list[i]))

while N * 24 > time and heap:
    b, a = heappop(heap)
    if (100 - a) // (-b) < 24 * N - time:
        tmp = a + (-b * ((100 - a) // (-b)))
        if tmp == 100:
            ans += 100
        else:
            heappush(heap, (-(100 - tmp), tmp))
        time += (100 - a) // (-b)
    else:
        ans += a + (N * 24 - time) * (-b)
        time += (N * 24 - time)

for b, a in heap:
    ans += a

print(ans)