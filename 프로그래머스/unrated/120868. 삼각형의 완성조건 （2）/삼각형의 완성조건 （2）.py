def solution(sides):
    answer = 0
    edge = abs(sides[0] - sides[1]) # 나머지 한 변의 길이가 될 수 있는 정수.
    
    while True:
        sides2 = sides + [edge] # 새 변까지 포함한 세 개의 변의 길이 리스트.
        sides2.sort() # 오름차순으로 정렬
        
        max_edge = max(sides2) # 가장 긴 변의 길이
        other_sum = sum(sides2[:2]) # 가장 긴 변을 제외한 나머지 두 변의 길이의 합
        
        # 가장 긴 변의 길이가 다른 두 변의 길이의 합보다 작을 경우
        # 삼각형을 만들 수 있으므로 answer에 1을 더합니다.
        if max_edge < other_sum:
            answer += 1
        # 케이스 체크 후 edge의 길이를 1 증가.
        edge += 1
        # 기존에 주어진 두 변의 길이보다 새 변의 길이가 크거나 같을 경우,
        # 더 이상 삼각형을 만들 수 없으므로 반복문을 종료합니다.
        if edge >= sum(sides):
            break

    return answer