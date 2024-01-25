m, n = map(int,input().split())
grid = [[0 for _ in range(n)] for _ in range(m)]
direction = {0:[0, 1], 1:[1, 0], 2:[0, -1], 3:[-1, 0]}

end = m * n - 2
cnt = 0
head = 0
i,j = 0,0
grid[i][j] = 1
while end >= 0:
    condi = False
    if 0 <= i + direction[head][0] < m and 0 <= j + direction[head][1] < n:
        if grid[i + direction[head][0]][j + direction[head][1]] != 1:
            grid[i + direction[head][0]][j + direction[head][1]] = 1
            i, j = i + direction[head][0], j + direction[head][1]
            condi = True
    if not condi:
        cnt += 1
        head = (head + 1) % 4
        i, j = i + direction[head][0], j + direction[head][1]
        grid[i][j] = 1
    end -= 1

print(cnt)