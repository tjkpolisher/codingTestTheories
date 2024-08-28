import sys
from collections import deque
input = sys.stdin.readline

T = int(input())


def flip(flag):
    return True if not flag else False


def direction_pop(flag, array):
    if flag:  # 뒤집힌 상태
        array.pop()
    else:  # 뒤집히지 않은 상태
        array.popleft()
    return array


for _ in range(T):
    p = input().rstrip()
    n = int(input())
    array = deque(input().rstrip()[1:-1].split(","))
    if not n:
        array = deque()

    is_flipped = False
    error_occured = False
    for i in range(len(p)):
        if p[i] == 'R':
            is_flipped = flip(is_flipped)
        elif p[i] == 'D':
            if not array:
                print("error")
                error_occured = True
                break
            array = direction_pop(is_flipped, array)
    if not error_occured:
        if is_flipped:
            array.reverse()
        print("[" + ",".join(array) + "]")