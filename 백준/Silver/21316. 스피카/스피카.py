import sys
input = sys.stdin.readline

graph = [[] for _ in range(13)]
for _ in range(12):
    x, y = map(int, input().split())
    # 양방향 그래프로 구성
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, 13):
    if len(graph[i]) != 3:
        continue
    adjacent_line = set(range(1, 4))
    for j in graph[i]:
        if len(graph[j]) not in adjacent_line:
            break
        else:
            adjacent_line.remove(len(graph[j]))
    if not adjacent_line:
        print(i)
        exit()