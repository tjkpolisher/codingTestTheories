def solution(board):
    def is_valid(num, row, col):
        # 현재 위치에 num이 들어갈 수 있는 지 검사
        return not (in_row(num, row) or
                    in_col(num, col) or
                    in_box(num, row, col))

    def in_row(num, row):
        # 해당 행에 num이 있는지 확인
        return num in board[row]

    def in_col(num, col):
        # 해당 열에 num이 있는지 확인
        return num in (board[i][col] for i in range(9))

    def in_box(num, row, col):
        # 현재 위치의 3 x 3 박스에 num이 있는지 확인
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return True
        return False

    def find_empty_position():
        # 스도쿠 보드에서 비어 있는 위치 반환
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def find_solution():
        # 비어 있는 위치에 가능한 숫자를 넣어가며 스도쿠 해결
        empty_pos = find_empty_position()
        # 빈 칸이 없으면 스도쿠가 해결된 것으로 간주
        if not empty_pos:
            return True
        row, col = empty_pos
        for num in range(1, 10):
            if is_valid(num, row, col):
                board[row][col] = num
                if find_solution():  # 다음 빈칸을 재귀 탐색
                    return True
                board[row][col] = 0  # 가능한 숫자가 없으면 원래의 0으로 되돌림
        return False

    find_solution()
    return board


if __name__ == "__main__":
    ex1 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
    ex2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    for e in [ex1, ex2]:
        print(solution(e))
