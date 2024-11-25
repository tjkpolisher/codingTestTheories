import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input().rstrip())

# 16개의 MBTI 조합
mbti = {'ENFP', 'ENFJ', 'ENTP', 'ENTJ',
        'ESFP', 'ESFJ', 'ESTP', 'ESTJ',
        'INFP', 'INFJ', 'INTP', 'INTJ',
        'ISFP', 'ISFJ', 'ISTP', 'ISTJ'}

cnt = 0
for i in range(N):
    for j in range(M):
        # 가로
        if j + 3 < M:
            string = board[i][j:j + 4]
            if string in mbti or string[::-1] in mbti:
                cnt += 1
        # 세로
        if i + 3 < N:
            string = board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 3][j]
            if string in mbti or string[::-1] in mbti:
                cnt += 1
        # 대각선
        if i + 3 < N and j + 3 < M:
            string = board[i][j] + board[i + 1][j + 1] + board[i + 2][j + 2] + board[i + 3][j + 3]
            if string in mbti or string[::-1] in mbti:
                cnt += 1
        if i + 3 < N and j - 3 >= 0:
            string = board[i][j] + board[i + 1][j - 1] + board[i + 2][j - 2] + board[i + 3][j - 3]
            if string in mbti or string[::-1] in mbti:
                cnt += 1
print(cnt)