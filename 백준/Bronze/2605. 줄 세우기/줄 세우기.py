n = int(input())
numbers = list(map(int, input().split()))
queue = []
for i, num in enumerate(numbers):
    if i == 0:
        queue.append(i + 1)
    else:
        queue.insert(i - num, i + 1)
for j in queue:
    print(j, end=' ')