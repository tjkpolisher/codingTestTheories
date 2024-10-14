from itertools import product


def solve(N, checkers):
    # 모든 가능한 x, y 좌표 조합 생성
    x_coords = sorted(set(x for x, _ in checkers))
    y_coords = sorted(set(y for _, y in checkers))

    # 결과를 저장할 리스트 초기화
    result = [float('inf')] * N

    # 모든 가능한 중심점에 대해 계산
    for center_x, center_y in product(x_coords, y_coords):
        # 각 체커에서 중심점까지의 거리 계산
        distances = sorted(abs(x - center_x) + abs(y - center_y) for x, y in checkers)

        # 누적 거리 계산
        total_distance = 0
        for i in range(N):
            total_distance += distances[i]
            # i+1개의 체커를 모으는데 필요한 최소 이동 횟수 갱신
            result[i] = min(result[i], total_distance)

    return result


# 입력 처리
N = int(input())
checkers = [list(map(int, input().split())) for _ in range(N)]

# 문제 해결 및 출력
print(*solve(N, checkers))