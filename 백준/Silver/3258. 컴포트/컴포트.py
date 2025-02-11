import sys
input = sys.stdin.readline

N, Z, M = map(int, input().split())

obstacles = set(map(int, input().split()))

for K in range(1, N):
    visited = set()
    pos = 1  # 시작 위치
    
    while pos not in visited:
        visited.add(pos)
        if pos in obstacles:
            break
        pos = (pos + K - 1) % N + 1
        if pos == Z:
            print(K)
            exit()