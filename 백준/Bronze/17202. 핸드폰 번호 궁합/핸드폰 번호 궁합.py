import sys
input = sys.stdin.readline

a = list(input().rstrip().split('-'))
b = list(input().rstrip().split('-'))

a = ''.join(a)
b = ''.join(b)

number = ''
for i in range(len(a)):
    number += a[i]
    number += b[i]

while len(number) > 2:
    ans = ''
    for i in range(len(number) - 1):
        tmp = int(number[i]) + int(number[i + 1])
        ans += str(tmp)[-1]
    number = ans
print(number)