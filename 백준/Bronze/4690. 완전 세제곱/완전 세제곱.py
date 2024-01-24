a = 2
while a <= 100:
    b, c, d = 1, 1, 1
    for b in range(2, a + 1):
        for c in range(b+1, a + 1):
            for d in range(c+1, a + 1):
                if a ** 3 == b ** 3 + c ** 3 + d ** 3:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
    a += 1