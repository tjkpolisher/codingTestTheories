import sys
input = sys.stdin.readline


# 부스터를 켰을 때 트랙을 도는 시간
def booster(X, v, v_b):
    '''
    Variables
    ========================================
    X: 트랙 길이
    v: 입력받은 나의 속도(아래의 v_N에 해당)
    v_b: 부스터 속도(최대값은 문제에서 주어진 Y)
    '''
    d = X - v_b
    return d / v + 1


T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    velocities = list(map(int, input().split()))
    v_N = velocities[-1]  # 나의 속도
    max_v = max(velocities)  # 입력받은 속도들 중 최고 속도

    if v_N == max_v:
        print(0)
        continue

    else:
        times = [X / v for v in velocities[:-1]]
        t_N = min(times)
        low, high = 0, Y

        while low <= high:
            mid = (low + high) // 2
            boost = booster(X, v_N, mid)
            if boost >= t_N:
                low = mid + 1
            else:
                high = mid - 1

        if low > Y:
            print(-1)
        else:
            print(low)