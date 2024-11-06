import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A_list = sorted(list(map(int, input().split())))
print(A_list[K - 1])