from collections import deque


def solution(maps):
    # 문제 출처: 프로그래머스 연습문제 - 미로 탈출
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/159993
    # 팁: 최단 경로 알고리즘을 떠오르게 하는 문제지만, 이 문제는 가중치가 있는 간선이 없습니다.
    # 너비 우선 탐색(BFS)는 항상 최단 경로를 보장하므로 BFS를 사용하면 문제를 풀 수 있습니다.

    n, m = len(maps), len(maps[0])
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque()
    end_y, end_x = -1, -1

    # 시작점과 도착점을 큐에 넣고 방문 여부 표시
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                q.append((i, j, 0, 0))
                visited[i][j][0] = True
            if maps[i][j] == 'E':
                end_y, end_x = i, j

    while q:
        y, x, k, time = q.popleft()  # 큐에서 좌표와 이동 횟수를 꺼냄

        if y == end_y and x == end_x and k == 1:
            return time

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not is_valid(ny, nx, n, m, maps):
                continue
            if maps[ny][nx] == "L":
                # 레버에 도달했을 경우
                append_to_queue(ny, nx, 1, time, visited, q)
            else:
                append_to_queue(ny, nx, k, time, visited, q)

    # 도착점에 도달하지 못한 경우
    return -1


def is_valid(ny, nx, n, m, maps):
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X'


def append_to_queue(ny, nx, k, time, visited, q):
    # 방문한 적이 없으면 큐에 넣고 방문 여부 표시
    if not visited[ny][nx][k]:
        visited[ny][nx][k] = True
        q.append((ny, nx, k, time + 1))


if __name__ == "__main__":
    ex1 = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
    ex2 = ["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]
    for e in [ex1, ex2]:
        print(solution(e))
