def solution(n):
    n_list = [int(str(n)[i]) for i in range(len(str(n)))]
    answer = sum(n_list)

    return answer