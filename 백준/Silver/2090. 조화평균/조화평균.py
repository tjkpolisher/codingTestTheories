from fractions import Fraction

N = int(input())
numbers = list(map(int, input().split()))

numbers_fraction_sum = [Fraction(1, numbers[i]) for i in range(N)]

if len(numbers_fraction_sum) > 1:
    harmony_average = Fraction(1, sum(numbers_fraction_sum))
    print(harmony_average)
else:
    print(f"{numbers[0]}/1")