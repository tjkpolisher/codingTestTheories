import sys
input = sys.stdin.readline

P = int(input())
for _ in range(P):
    data = list(map(int, input().split()))
    T = data[0]
    sequence = data[1:]

    stack = [0]
    island_count = 0

    for num in sequence:
        while stack and stack[-1] > num:
            stack.pop()
            island_count += 1

        if stack and stack[-1] == num:
            continue
        else:
            stack.append(num)

    print(T, island_count)