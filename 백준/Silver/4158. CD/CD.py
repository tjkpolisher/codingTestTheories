import sys
input = sys.stdin.readline
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    cd_set1 = set()
    cd_set2 = set()
    cnt = 0
    
    for _ in range(N):
        cd_set1.add(int(input()))
    
    for _ in range(M):
        n = int(input())
        if n in cd_set1:
            cnt += 1
    
    print(cnt)