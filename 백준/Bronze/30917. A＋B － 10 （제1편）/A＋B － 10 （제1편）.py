def solution():
    for a in range(1, 10):
        print("? A", a, flush=True)

        resp = int(input())

        if resp == 1:
            for b in range(1, 10):
                print("? B", b, flush=True)
                resp2 = int(input())
                if resp2 == 1:
                    return f"! {a + b}"
    return f"! {a + b}"


print(solution())