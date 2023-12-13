import sys
input = sys.stdin.readline
A, B = map(int, input().split())

# A < B일 때를 기준으로 로직 작성
if A >= B:
    A, B = B, A

n = B - A + 1
result = n * (A + B) // 2

print(result)