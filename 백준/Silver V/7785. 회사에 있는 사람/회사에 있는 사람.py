n = int(input())
table = {}

for _ in range(n):
    name, is_in = input().split()
    table[name] = is_in

names = [n for n in table.keys() if table[n] == 'enter']
names.sort(reverse=True)
for n in names:
    print(n)