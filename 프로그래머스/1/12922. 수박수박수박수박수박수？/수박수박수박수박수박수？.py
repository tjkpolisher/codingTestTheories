def solution(n):
    answer = []
    for i in range(n):
        if i % 2 == 0:
            answer.append('수')
        else:
            answer.append('박')
    answer = ''.join(answer)
    return answer