def solution(arr):
    answer = []
    for a in arr:    
        if not answer or answer[-1] != a:
            answer.append(a)
    return answer