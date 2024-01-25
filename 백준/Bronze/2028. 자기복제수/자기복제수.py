T = int(input())
for i in range(T):
    N = input()
    N_squared = int(N) ** 2
    
    if str(N_squared)[-len(N):] == N:
        print('YES')
    else:
        print('NO')