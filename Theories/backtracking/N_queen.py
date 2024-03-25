# 문제 출처: 프로그래머스 연습문제 - N-Queen
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12952


def get_answer(n, y, width, diagonal1, diagonal2):
    """get_answer
    Args:
        n: 체스판의 크기
        y: 현재 퀸을 놓을 위치
        width: 특정 열에 퀸이 위치했는지 표시
        diagonal1: 오른쪽 위에서 왼쪽 아래 방향 대각선 방향 퀸 중복 체크용 배열
        diagonal2: 왼쪽 위에서 오른쪽 아래 방향 대각선 방향 퀸 중복 체크용 배열

    Returns:
        answer: 정답
    """
    ans = 0
    # 모든 행에 대하여 퀸의 위치가 결정되었을 경우
    if y == n:
        # 정답에 1 증가
        ans += 1
    else:
        # 현재 행에서 퀸이 놓일 수 있는 모든 위치를 시도
        for i in range(n):
            # 해당 위치에 이미 퀸이 있는 경우는 건너뛰기
            if width[i] or diagonal1[i + y] or diagonal2[i - y + n]:
                continue

            # 해당 위치에 퀸을 놓음
            width[i] = diagonal1[i + y] = diagonal2[i - y + n] = True
            # 다음 행으로 이동하여 재귀적으로 해결 가능한 경우의 수 찾기
            ans += get_answer(n, y + 1, width, diagonal1, diagonal2)
            # 해당 위치에 놓인 퀸을 제거
            width[i] = diagonal1[i + y] = diagonal2[i - y + n] = False
    return ans


def solution(n):
    ans = get_answer(n, 0, [False] * n, [False] * (n * 2), [False] * (n * 2))
    return ans


if __name__ == "__main__":
    ex1 = 4

    print(solution(ex1))
