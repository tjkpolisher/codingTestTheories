def solution(i, j, k):
    answer = 0
    k = str(k)
    for num in range(i, j + 1):
        ls = list(str(num))
        for idx in range(len(ls)):
            if ls[idx] == k:
                answer += 1
    return answer