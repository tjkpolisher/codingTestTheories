N = int(input())
size = []  # 덩치를 판단하는 두 수치를 저장할 리스트
for _ in range(N):
    x, y = map(int, input().split())
    size.append([x, y])

for i in size:
    rank = 1
    for j in size:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')