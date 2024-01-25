def solution(score):
    avgt2 = [score_i[0]+score_i[1] for score_i in score] # 평균 점수 * 2
    avg_sort = sorted(avgt2, reverse=True) # 내림차순으로 평균 점수 정렬
    
    raw_rank = [avg_sort.index(avgt2[i]) + 1 for i in range(len(score))]
    answer = []
    
    return raw_rank