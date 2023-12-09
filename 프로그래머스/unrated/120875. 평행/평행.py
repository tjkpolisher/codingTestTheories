def solution(dots):
    from itertools import combinations
    from fractions import Fraction
    answer = 0
    
    # 4개의 점 중 2개를 선택하는 모든 조합을 생성
    for line1 in combinations(dots, 2):
        # 선택되지 않은 나머지 2개의 점을 이용하여 두 번째 직선을 형성
        rest_dots = [dot for dot in dots if dot not in line1]  # line1에 포함되지 않은 점 추출
        line2 = rest_dots  # 나머지 두 점으로 line2 형성

        x1, y1, x2, y2 = line1[0][0], line1[0][1], line1[1][0], line1[1][1]
        x3, y3, x4, y4 = line2[0][0], line2[0][1], line2[1][0], line2[1][1]

        # 두 직선의 기울기 계산
        if x1 == x2:  # line1이 수직선인 경우
            incline1 = 'inf'
        else:
            incline1 = Fraction(y2 - y1, x2 - x1)

        if x3 == x4:  # line2가 수직선인 경우
            incline2 = 'inf'
        else:
            incline2 = Fraction(y4 - y3, x4 - x3)

        # 두 직선의 기울기가 같으면 평행하므로 answer에 1을 할당하고 반복문을 종료
        if incline1 == incline2:
            answer = 1
            break

    return answer