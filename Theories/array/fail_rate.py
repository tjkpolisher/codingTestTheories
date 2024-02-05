def solution(N, stages):
    # 문제 출처: 2019 KAKAO BLIND RECRUITMENT
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42889
    # 실패율 정의: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
    
    # 스테이지 별 도전자 수
    challenger = [0] * (N + 2) # 0을 맨 앞에 추가함으로써 각 번호 자체를 인덱스로 활용 가능
    for stage in stages:
        challenger[stage] += 1
    
    # 스테이지 별 실패한 사용자 수 집계 및 실패율 계산
    fails = {}
    total = len(stages)
    for i in range(1, N + 1):
        if challenger[i] == 0:
            # 도전한 사람이 없는 경우, 실패율은 0
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]
    
    result = sorted(fails, key=lambda x: fails[x], reverse=True)
    
    return result

if __name__ == "__main__":
    ex1 = [5, [2, 1, 2, 6, 2, 4, 3, 3]]
    ex2 = [4, [4, 4, 4, 4, 4]]
    for e in [ex1, ex2]:
        print(solution(e[0], e[1]))