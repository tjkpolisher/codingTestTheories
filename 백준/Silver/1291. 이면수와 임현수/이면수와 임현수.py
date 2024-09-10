N = int(input())


def im_yeon_su(N):
    # 이면수 판정 함수
    if N <= 5:
        return False
    N_str = str(N)
    summation = 0
    for i in range(len(N_str)):
        summation += int(N_str[i])
    return True if summation % 2 != 0 else False


def im_hyeon_su(N):
    # 임현수 판정 함수
    if N == 4 or N == 2:
        return True
    if N == 1:
        prime_factors = [1]
    else:
        prime_factors = prime_factorization(N)
    return True if len(prime_factors) % 2 == 0 else False


def prime_factorization(N):
    # 소인수를 리스트 형태로 반환하는 함수
    prime_factors = []
    p = 2
    while p <= N:
        if N % p == 0:
            if p not in prime_factors:
                prime_factors.append(p)
            N //= p
        else:
            p += 1
    return prime_factors


im = im_yeon_su(N)
ih = im_hyeon_su(N)

if im and ih:
    # 이면수이면서 임현수일 경우
    print(4)
elif im and not ih:
    # 이면수이지만 임현수가 아닐 경우
    print(1)
elif not im and ih:
    # 임현수이지만 이면수가 아닐 경우
    print(2)
else:
    # 둘 다 아닌, 즉 성경수일 경우
    print(3)