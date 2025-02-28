N = int(input())
if N == 1:
    print(2)
    exit()

# 소수만 남기는 집합 연산
prime = set(range(2, N + 1))
for i in range(2, int((N + 1) ** 0.5) + 1):
    if i in prime:
        prime -= set(range(2 * i, N + 1, i))


def is_prime(num):
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    return True


tmp = N
while True:
    if is_prime(tmp):
        prime.add(tmp)

    str_tmp = str(tmp)
    if str_tmp == str_tmp[::-1] and tmp in prime:
        print(tmp)
        break
    tmp += 1