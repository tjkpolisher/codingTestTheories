import sys
input = sys.stdin.readline

N = int(input())
number_list = []
for _ in range(N):
    number_list.append(input().rstrip()[::-1])

length = len(number_list[0])  # 모든 학생의 번호의 길이는 동일
for i in range(1, length):
    sliced_set = set()

    for j in range(N):
        sliced_set.add(number_list[j][:i])

    if len(sliced_set) == N:
        ans = i
        break
else:
    ans = length

print(ans)