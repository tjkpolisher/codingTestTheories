def solution(maps):
    # 문제 출처: 프로그래머스 깊이/너비 우선 탐색(DFS/BFS) - 게임 맵 최단거리
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/1844
    from collections import deque
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    n = len(maps)
    m = len(maps[0])

    dist = [[-1] * m for _ in range(n)]

    def bfs(start):
        q = deque([start])
        dist[start[0]][start[1]] = 1

        while q:
            here = q.popleft()

            for direct in move:
                row = here[0] + direct[0]
                col = here[1] + direct[1]
                # 맵의 범위를 벗어나는 경우
                if row < 0 or row >= n or col < 0 or col >= m:
                    continue
                # 이동한 위치에 벽이 있는 경우(그래프의 값이 0)
                if not maps[row][col]:
                    continue
                # 이동한 위치에 처음 방문하는 경우
                if dist[row][col] == -1:
                    q.append([row, col])
                    dist[row][col] = dist[here[0]][here[1]] + 1

        return dist

    bfs([0, 0])
    return dist[n - 1][m - 1]


if __name__ == "__main__":
    ex1 = [[1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1],
           [1, 0, 1, 1, 1],
           [1, 1, 1, 0, 1],
           [0, 0, 0, 0, 1]]
    ex2 = [[1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1],
           [1, 0, 1, 1, 1],
           [1, 1, 1, 0, 0],
           [0, 0, 0, 0, 1]]
    for e in [ex1, ex2]:
        print(solution(e))
