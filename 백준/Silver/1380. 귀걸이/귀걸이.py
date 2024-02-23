scene_num = 0
while True:
    scene_num += 1
    n = int(input())
    if n == 0:
        break

    names = []
    for _ in range(n):
        names.append(input())
    index_stack = dict()

    for i in range(2 * n - 1):
        idx, c = input().split()
        idx = int(idx)
        if idx not in index_stack:
            index_stack[idx] = [c]
        else:
            index_stack.pop(idx, None)

    i = list(index_stack.keys())[0]
    print(scene_num, names[i - 1])