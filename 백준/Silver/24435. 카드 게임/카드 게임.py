import sys
from itertools import permutations
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    bob = input().rstrip()
    alice = list(input().rstrip())

    target = min(int(bob), int(''.join(list(bob)[::-1])))

    stop_flag = False
    prev_value = None
    for i in range(max(1, n - 2), n + 1):
        perms = sorted(list(permutations(alice, i)))
        # print(f"{perms=}")
        for perm in perms:
            tmp = int(''.join(perm))
            # print(f"{tmp=}")
            if tmp >= target:
                print(prev_value)
                stop_flag = True
                break
            prev_value = tmp

        if stop_flag:
            break
        else:
            prev_value = tmp
    else:
        print(prev_value)