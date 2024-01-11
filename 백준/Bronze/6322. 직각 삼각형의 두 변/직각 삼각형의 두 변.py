import math
number = 0
while True:
    number += 1
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    x_index = (a, b, c).index(-1)
    lines = ["a", "b", "c"]
    
    print(f"Triangle #{number}")
    if c != -1 and (a >= c or b >= c):
        print("Impossible.")
        print()
    else:
        if x_index == 2:
            ans = math.sqrt(a ** 2 + b ** 2)
        elif x_index == 0:
            ans = math.sqrt(c ** 2 - b ** 2)
        else:
            ans = math.sqrt(c ** 2 - a ** 2)
        print(f"{lines[x_index]} = {ans:.3f}")
        print()