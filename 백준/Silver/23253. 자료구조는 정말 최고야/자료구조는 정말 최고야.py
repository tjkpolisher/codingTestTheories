import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
# stacks = []
# tops = {}

for i in range(M):
    k_i = int(input())
    stack = list(map(int, input().rstrip().split()))
    if sorted(stack, reverse=True) != stack:
        print("No")
        break
else:
    print("Yes")