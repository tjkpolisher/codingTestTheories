N = int(input())
for i in range(N):
    S = int(input())
    factors = []
    j = 2
    answer = "YES"
    while j <= 10**6:
        if S % j == 0:
            if j <= 10**6:
                answer = "NO"
                break
        else:
            j += 1
    
    print(answer)