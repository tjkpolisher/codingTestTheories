N = input()
length = len(N)
N = int(N)


def first_term(length):
    ans = [0, 0, 9]
    for i in range(2, length + 1):
        term = ans[-1] + i * (10 ** i - 1 - (10 ** (i - 1) - 1))
        ans.append(term)
    return ans[-1]


if length > 1:
    ans = first_term(length - 1) + length * (N - (10 ** (length - 1) - 1))
else:
    ans = N
print(ans)