import sys
input = sys.stdin.readline

L = int(input())
string = input().rstrip()
characters = "abcdefghijklmnopqrstuvwxyz"
c_to_a = {characters[i]: i + 1 for i in range(len(characters))}
r = 31
result = 0
M = 1234567891
for i, c in enumerate(string):
    a = c_to_a[c]
    result += (a * r ** i)

result %= M
print(result)