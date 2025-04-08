C, P = map(int, input().split())
current_heights = list(map(int, input().split()))


def count_blocks(patterns):
    cnt = 0
    for length, condition in patterns:
        for i in range(C - length + 1):
            if condition(i):
                cnt += 1
    return cnt


def block1():
    return count_blocks([
        (1, lambda i: current_heights[i] >= 0),
        (4, lambda i: current_heights[i] == current_heights[i + 1] == current_heights[i + 2] == current_heights[i + 3])
    ])


def block2():
    return count_blocks([
        (2, lambda i: current_heights[i] == current_heights[i + 1])
    ])


def block3():
    return count_blocks([
        (3, lambda i: current_heights[i] == current_heights[i+1] == current_heights[i+2] - 1),
        (2, lambda i: current_heights[i] - 1 == current_heights[i+1])
    ])


def block4():
    return count_blocks([
        (3, lambda i: current_heights[i] - 1 == current_heights[i+1] == current_heights[i+2]),
        (2, lambda i: current_heights[i] == current_heights[i+1] - 1)
    ])


def block5():
    return count_blocks([
        (3, lambda i: current_heights[i] == current_heights[i+1] == current_heights[i+2]),
        (3, lambda i: current_heights[i] - 1 == current_heights[i+1] == current_heights[i+2] - 1),
        (2, lambda i: current_heights[i] - 1 == current_heights[i+1]),
        (2, lambda i: current_heights[i] == current_heights[i+1] - 1)
    ])


def block6():
    return count_blocks([
        (3, lambda i: current_heights[i] == current_heights[i+1] == current_heights[i+2]),
        (2, lambda i: current_heights[i] - 2 == current_heights[i+1]),
        (3, lambda i: current_heights[i] == current_heights[i+1] - 1 == current_heights[i+2] - 1),
        (2, lambda i: current_heights[i] == current_heights[i+1])
    ])


def block7():
    return count_blocks([
        (3, lambda i: current_heights[i] == current_heights[i+1] == current_heights[i+2]),
        (2, lambda i: current_heights[i] == current_heights[i+1]),
        (3, lambda i: current_heights[i] - 1 == current_heights[i+1] - 1 == current_heights[i+2]),
        (2, lambda i: current_heights[i] == current_heights[i+1] - 2)
    ])


if P == 1:
    print(block1())
elif P == 2:
    print(block2())
elif P == 3:
    print(block3())
elif P == 4:
    print(block4())
elif P == 5:
    print(block5())
elif P == 6:
    print(block6())
else:
    print(block7())