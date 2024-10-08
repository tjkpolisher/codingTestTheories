import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

array.sort()

temp = []
for i in range(N):
    cnt = 0
    for j in range(array[i], array[i] + 5):
        if j not in array:
            cnt += 1
    temp.append(cnt)

print(min(temp))