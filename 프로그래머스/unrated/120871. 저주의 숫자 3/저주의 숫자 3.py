def solution(n):
    answer = 0
    for _ in range(1, n + 1):
        answer += 1
        # 3의 배수이거나 3을 자릿수에 포함할 경우, 조건에서 벗어날 때까지 1을 더합니다.
        while '3' in str(answer) or answer % 3 == 0:
            answer += 1
        
    return answer