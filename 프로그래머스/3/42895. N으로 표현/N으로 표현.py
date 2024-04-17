def solution(N, number):
    if N == number:
        return 1
    
    # 최소값이 8보다 크면 어차피 -1을 리턴해야 함
    dp = [set() for i in range(8)]
    # 8개의 집합 초기화 (N, NN, ... NNNNNNNN)
    for i, x in enumerate(dp):
        x.add(int(str(N) * (i + 1)))
        
    for i in range(len(dp)): 
        for j in range(i):
            # op1 : 피연산자1, N을 j + 1번 사용하여 만들 수 있는 숫자들
            for op1 in dp[j]:
                # op2 : 피연산자2, N을 i - j번 사용하여 만들 수 있는 숫자들
                for op2 in dp[i - j - 1]: 
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        # number가 존재한다면 i + 1을 리턴
        if number in dp[i]:
            answer = i + 1
            break
        # 존재하지 않는다면 8을 넘게 되므로 -1 리턴
        else:
            answer = -1
    return answer