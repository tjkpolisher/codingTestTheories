import sys
input = sys.stdin.readline

for i in range(3, 0, -1):
    x = input().rstrip()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x) + i

if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)