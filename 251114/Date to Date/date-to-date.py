m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days1 = sum(num_days[:m1]) + d1
days2 = sum(num_days[:m2]) + d2

print(days2 - days1 + 1)