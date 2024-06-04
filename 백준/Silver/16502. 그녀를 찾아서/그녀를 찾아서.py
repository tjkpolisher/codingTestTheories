t = int(input())
M = int(input())

# 각 노드 별 이동 확률을 저장할 인접행렬 생성
matrix = [[0.0 for _ in range(4)] for _ in range(4)]
for _ in range(M):
    start, end, prob = input().split()
    i, j = ord(start) - ord('A'), ord(end) - ord('A')
    matrix[i][j] = float(prob)

current_prob = [0.25] * 4


def update_prob(matrix, current_prob):
    new_prob = [0.0] * 4
    for i in range(4):
        for j in range(4):
            new_prob[j] += current_prob[i] * matrix[i][j]
    return new_prob


for _ in range(t):
    current_prob = update_prob(matrix, current_prob)

for prob in current_prob:
    print(f"{prob * 100:.2f}")