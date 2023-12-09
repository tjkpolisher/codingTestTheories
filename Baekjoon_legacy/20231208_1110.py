# 1110: 더하기 사이클
N = int(input())
if N < 10:
    n1, n2 = 0, N
else:
    n1, n2 = N // 10, N % 10

counter = 0
while True:
    new_num = n2 * 10 + (n1 + n2) % 10
    counter += 1
    
    if new_num == N:
        break
    if new_num < 10:
        n1, n2 = 0, new_num
    else:
        n1, n2 = new_num // 10, new_num % 10
    
print(counter)