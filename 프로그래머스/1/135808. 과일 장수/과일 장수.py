def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    score = score[:m * (len(score) // m)]
    
    for i in range(len(score) // m):
        box = score[m * i:m * (i + 1)]
        minimum_score = min(box)
        answer += minimum_score * m
    return answer