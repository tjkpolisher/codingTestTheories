def is_valid(yellow, h):
    # 주어진 노란색 격자들이 카펫 안에 들어가는지 확인하는 함수
    if yellow % (h - 2) != 0:
        return False
    else:
        return True


def solution(brown, yellow):
    # 입력: 갈색 격자와 노란색 격자의 수
    # 출력: 카펫의 가로, 세로 크기
    for v in range(3, brown + yellow + 1):
        # 카펫 전체의 세로 길이를 바꿔가면서 비교
        # 카펫의 가로 길이는 세로 길이와 같거나 길어야 함
        if (brown + yellow) % v != 0:
            # 전체 격자의 개수가 세로 길이로 나누어 떨어져야 연산 실행 가능
            continue
        h = (brown + yellow) // v  # 카펫의 가로 길이
        if is_valid(yellow, h):
            return [h, v]