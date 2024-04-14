M, N = map(int, input().split())
number_set = set(range(M, N + 1))
if 1 in number_set:
    number_set -= set([1])

for i in range(2, N + 1):
    prime_numbers = set(range(i * 2, N + 1, i))
    number_set -= prime_numbers

number_set = list(number_set)
number_set.sort()
for n in number_set:
    print(n)