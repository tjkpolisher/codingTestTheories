P, N = map(int, input().split())
squares = {i: 0 for i in range(1, P + 1)}
order = True  # 백돌/흑돌 순서(True일 경우 Mirko의 백돌을 놓을 차례)

for i in range(N):
    move = int(input())
    # 현재 플레이어 색 결정
    color = 'w' if order else 'b'
    opponent = 'b' if order else 'w'

    squares[move] = color  # 현재 돌 놓기

    # 왼쪽 방향 검사
    temp_positions = []
    for pos in range(move - 1, 0, -1):
        if squares[pos] == opponent:
            # 상대 돌이 연속되는 중
            temp_positions.append(pos)
        elif squares[pos] == color:
            # 동일 색 돌 발견 -> 사이의 상대 돌 제거
            if temp_positions:
                for p in temp_positions:
                    squares[p] = 0
            break
        else:
            # 빈 칸 혹은 아무것도 아니면(사실 0만 가능) 중단
            break

    # 오른쪽 방향 검사
    temp_positions = []
    for pos in range(move + 1, P + 1):
        if squares[pos] == opponent:
            temp_positions.append(pos)
        elif squares[pos] == color:
            # 동일 색 돌 발견 -> 사이의 상대 돌 제거
            if temp_positions:
                for p in temp_positions:
                    squares[p] = 0
            break
        else:
            # 빈 칸이면 중단
            break

    order = not order

result = list(squares.values())
print(result.count('w'), result.count('b'))