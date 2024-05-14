import sys
input = sys.stdin.readline

X, Y = map(int, input().rstrip().split())


def calculate_win_rate(X, Y):
    return (Y * 100) // X


def minimum_additional_games(X, Y):
    current_win_rate = calculate_win_rate(X, Y)
    if current_win_rate >= 99:
        return -1

    left, right = 1, 1000000000
    result = -1

    while left <= right:
        mid = (left + right) // 2
        new_X = X + mid
        new_Y = Y + mid
        new_win_rate = calculate_win_rate(new_X, new_Y)

        if new_win_rate > current_win_rate:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


# 결과 출력
print(minimum_additional_games(X, Y))