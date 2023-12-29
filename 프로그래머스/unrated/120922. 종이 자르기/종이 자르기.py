def solution(M, N):
    if M == 1 and N == 1:
        answer = 0
    else:
        answer = M * N - 1
    return answer