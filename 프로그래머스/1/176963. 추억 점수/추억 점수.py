def solution(name, yearning, photo):
    answer = []
    name_score = dict(zip(name, yearning))
    for i in range(len(photo)):
        score = 0 # 추억 점수
        p = photo[i] # photo 목록 중 인덱스 i인 사진
        if sorted(name) == sorted(p): # 사진 속 인물이 name 목록과 동일할 때
            score = sum(yearning)
        else:
            for n in p: # 사진 p에 있는 인물들 중
                if n in name: # 사진에 있는 인물이 name에 있는 인물일 경우
                    s = name_score[n]
                    score += s
        answer.append(score)            
    return answer