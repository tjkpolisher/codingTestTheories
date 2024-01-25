def solution(n):
    n = str(n)
    
    answer = [int(n[i]) for i in range(len(n))][::-1]
    return answer