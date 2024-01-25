n = int(input())
numbers = []
for i in range(n):
    numbers.append(list(map(int, input().split())))

companion = [[0 for i in range(n)] for j in range(n)] # 같은 반이었던 학생 수
for i in range(5):
    for j in range(n):
        for k in range(j + 1, n):
            if numbers[j][i] == numbers[k][i]:
                companion[j][k] = 1
                companion[k][j] = 1

frequency = []
for c in companion:
    frequency.append(c.count(1))

print(frequency.index(max(frequency)) + 1)