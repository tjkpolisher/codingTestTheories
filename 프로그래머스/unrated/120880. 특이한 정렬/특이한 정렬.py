def solution(numlist, n):
    distances = [abs(num - n) for num in numlist]
    dict_dist = {numlist[i] : distances[i] for i in range(len(numlist))}
    d = dict_dist.items()
    d = sorted(d, key=lambda x: x[1])
    # answer = [d[i][0] for i in range(len(d))]
    answer = []
    for i in range(len(d)):
        answer.append(d[i][0])
        if i > 0 and (d[i-1][0] < d[i][0] and d[i-1][1] == d[i][1]):
            answer[i-1], answer[i] = answer[i], answer[i-1]
    
    return answer