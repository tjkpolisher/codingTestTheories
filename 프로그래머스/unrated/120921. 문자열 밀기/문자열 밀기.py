def solution(A, B):
    answer = -1
    counter = 0
    if A == B:
        answer = counter
    else:
        while counter < len(A):
            counter += 1
            pushed = []
            pushed.append(A[-1])
            for i in range(len(A) - 1):
                pushed.append(A[i])
            A = ''.join(pushed)
            if A == B:
                answer = counter
                break
    return answer