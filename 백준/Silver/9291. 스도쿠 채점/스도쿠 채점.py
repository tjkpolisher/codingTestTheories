T = int(input())


def is_valid_sudoku(grid):
    # 행 검사
    for row in grid:
        if len(set(row)) != 9 or sum(row) != 45:
            return False

    # 열 검사
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if len(set(column)) != 9 or sum(column) != 45:
            return False

    # 3x3 그룹 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            group = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(group)) != 9 or sum(group) != 45:
                return False

    return True


for case in range(1, T + 1):
    grid = []
    for _ in range(9):
        row = list(map(int, input().split()))
        grid.append(row)
    
    result = "CORRECT" if is_valid_sudoku(grid) else "INCORRECT"
    print(f"Case {case}: {result}")
    
    if case < T:
        input()  # 빈 줄 처리