import sys
from collections import deque
input = sys.stdin.readline

A, B = input().rstrip().split()
ret = []
for i in range(len(B) - len(A) + 1):
	cnt = 0
	for j in range(len(A)):
		if A[j] != B[i + j]:
			cnt += 1
	ret.append(cnt)
print(min(ret))