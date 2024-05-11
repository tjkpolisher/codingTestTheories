n = int(input())
paper = [[0] * 100 for _ in range(100)]  # 하얀 도화지 (색종이가 덮이지 않은 초기 상태가 0)
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for j in range(10):
        for i in range(10):
            if (0 <= 100 - y - 10 + j < 100 and 0 <= x + i < 100) and not paper[100 - y - 10 + j][x + i]:
                paper[100 - y - 10 + j][x + i] = 1
                cnt += 1

print(cnt)