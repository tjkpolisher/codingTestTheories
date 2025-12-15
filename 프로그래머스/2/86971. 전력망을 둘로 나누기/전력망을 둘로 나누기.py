from collections import deque
def solution(n, wires):
    answer = float('inf')
    
    def bfs(node, graph, visited):
        q = deque([node])
        cnt = 0
        visited[node] = True
        
        while q:
            p = q.popleft()
            cnt += 1
            for neighbor in graph[p]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
        
        return cnt
    
    for i, wire in enumerate(wires):
        graph = {k: [] for k in range(1, n + 1)}
        visited = [False] * (n + 1)
        
        for j, (v1, v2) in enumerate(wires):
            if i == j:  # i번째 전선 끊기
                continue
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        # 첫 번째 전력망 크기
        size1 = bfs(1, graph, visited)

        # 두 번째 전력망 크기
        size2 = n - size1

        # 두 전력망 크기의 차이를 계산
        answer = min(answer, abs(size1 - size2))
    
    return answer