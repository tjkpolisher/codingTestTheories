from itertools import permutations


def is_solvable(a, b, c, d):
    nums = [a, b, c]
    for k in range(1, 4):
        for p in permutations(nums, k):
            if k == 1:
                if p[0] == d:
                    return True

            elif k == 2:
                x, y = p[0], p[1]
                if x + y == d:
                    return True
                if x - y == d:
                    return True
                if x * y == d:
                    return True
                if y != 0 and x % y == 0 and x // y == d:
                    return True

            elif k == 3:
                x, y, z = p[0], p[1], p[2]
                res1_options = {x + y, x - y, x * y}
                if y != 0 and x % y == 0:
                    res1_options.add(x // y)

                for res1 in res1_options:
                    if res1 + z == d:
                        return True
                    if res1 - z == d:
                        return True
                    if res1 * z == d:
                        return True
                    if z != 0 and res1 % z == 0 and res1 // z == d:
                        return True

                res2_options = {y + z, y - z, y * z}
                if z != 0 and y % z == 0:
                    res2_options.add(y // z)

                for res2 in res2_options:
                    if x + res2 == d:
                        return True
                    if x - res2 == d:
                        return True
                    if x * res2 == d:
                        return True
                    if res2 != 0 and x % res2 == 0 and x // res2 == d:
                        return True

    return False


d = int(input())
for a in range(1, 101):
    for b in range(1, 101):
        for c in range(1, 101):
            if len({a, b, c, d}) != 4:
                continue
            if not is_solvable(a, b, c, d):
                print(a, b, c)
                exit()