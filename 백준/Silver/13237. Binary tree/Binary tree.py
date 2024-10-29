n = int(input())
nodes = []
for _ in range(n):
    nodes.append(int(input()))

height = [0] * n

for i in range(n):
    # 루트 노드의 높이는 0
    if nodes[i] == -1:
        continue
    height[i] = height[nodes[i] - 1] + 1

for h in height:
    print(h)