from random import shuffle

def solution():
    num_li = list(range(1, 10001))
    shuffle(num_li)
    for a in num_li:
        print("? A", a, flush=True)
        resp = int(input())
        if resp:
            break

    for b in num_li:
        print("? B", b, flush=True)
        resp2 = int(input())
        if resp2:
            return f"! {a + b}"
    return f"! {a + b}"


print(solution())