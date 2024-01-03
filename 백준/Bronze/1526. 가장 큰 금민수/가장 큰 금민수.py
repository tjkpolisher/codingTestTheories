from itertools import product
N = input()
length = len(N)
N = int(N)
sets = ['4', '7']
gold = []
for i in range(1, length + 1):
    nums = product(sets, repeat=i)
    for num in nums:
        n = int(''.join(num))
        gold.append(n)
gold = [g for g in gold if g <= N]
print(max(gold))