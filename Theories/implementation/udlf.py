def solution(n, plan):
    point = [0, 0]  # X, Y 좌표의 인덱스
    plan_list = list(plan.split())
    for p in plan_list:
        if p == "R" and (0 <= point[0] + 1 < N):
            point[0] += 1
        elif p == "L" and (0 <= point[0] - 1 < N):
            point[0] -= 1
        elif p == "D" and (0 <= point[1] + 1 < N):
            point[1] += 1
        elif p == "U" and (0 <= point[1] - 1 < N):
            point[1] -= 1

    return point[1] + 1, point[0] + 1


if __name__ == "__main__":
    N = 5
    plan = "R R R U D D"
    print(solution(N, plan))  # 정답: 3 4
