import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(graph, node, target, depth, visited, values):
    """dfs 함수

    Args:
        graph: DFS를 수행할 그래프. 이 문제에서는 트리가 되겠습니다.
        node: DFS를 시작할 기준이 되는 정점(노드).
        target: 찾고자 하는 값(k).
        depth: 트리의 깊이. 기본값 0부터 시작해 재귀를 거듭하면서 1씩 증가시킵니다.
        visited: 방문 여부를 저장하는 리스트.
        values: 각 노드에 저장된 값을 저장한 리스트.

    Returns:
        Boolean: 트리의 분기에서 해당 값을 찾은 경우 True를, 못 찾은 경우 False를 반환.
    """
    visited[node] = True
    if values[node] == target:
        print(depth)
        return True  # 찾은 경우 True 반환
    for i in graph[node]:
        if not visited[i]:
            if dfs(graph, i, target, depth + 1, visited, values):
                return True  # 하위 호출에서 찾은 경우 상위 호출로 True 전파
    return False  # 해당 경로에서 찾지 못한 경우 False 반환


n, k = map(int, input().split())

# 트리 생성
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    p, c = map(int, input().split())
    tree[p].append(c)

values = list(map(int, input().split()))
visited = [False] * n

# DFS 수행
dfs(tree, 0, k, 0, visited, values)