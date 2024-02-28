# defaultdict: 키가 없을 때 기본값을 defaultdict 형태로 기본값을 지정
from collections import defaultdict


def solution(graph, start):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    visited = set()
    result = []
    dfs(start, visited, adj_list, result)
    return result


def dfs(node, visited, adj_list, result):
    visited.add(node)
    result.append(node)
    for neighbor in adj_list.get(node, []):
        if neighbor not in visited:
            dfs(neighbor, visited, adj_list, result)


if __name__ == "__main__":
    ex1 = [[['A', 'B'], ['B', 'C'],
            ['C', 'D'], ['D', 'E']],
           'A']
    ex2 = [[['A', 'B'], ['A', 'C'],
            ['B', 'D'], ['B', 'E'],
            ['C', 'F'], ['E', 'F']],
           'A']
    for e in [ex1, ex2]:
        print(solution(e[0], e[1]))
