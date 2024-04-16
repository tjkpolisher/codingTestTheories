import sys
from collections import deque
input = sys.stdin.readline


def solution():
    q = deque()
    balls = 0
    walls = 0
    direction = 0  # 0: 가로, 1: 세로(위에서 아래로), 2: 가로(반대), 3: 세로(아래에서 위로)

    for _ in range(Q):
        query = input().split()

        if query[0] == 'push':
            item = query[1]
            if (direction == 0 or direction == 2):
                q.appendleft(item)
                if item == 'b':
                    balls += 1
                else:
                    walls += 1
            elif direction == 1:
                if item == 'b':
                    if q and q[-1] == 'w':
                        balls += 1
                        q.appendleft(item)
                else:
                    walls += 1
                    q.appendleft(item)
            elif direction == 3:
                if item == 'w':
                    walls += 1
                    q.appendleft(item)
        elif query[0] == 'pop':
            if q:
                if direction == 1:
                    if q[-1] == 'w':
                        q.pop()
                        walls -= 1
                        while q and q[-1] == 'b':
                            q.pop()
                            balls -= 1
                else:
                    item = q.pop()
                    if item == 'b':
                        balls -= 1
                    else:
                        walls -= 1
        elif query[0] == 'rotate':
            if query[1] == 'l':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
            if direction == 1:
                while q and q[-1] == 'b':
                    q.pop()
                    balls -= 1
            elif direction == 3:
                while q and q[0] == 'b':
                    q.popleft()
                    balls -= 1
        elif query[0] == 'count':
            if query[1] == 'b':
                print(balls)
            else:
                print(walls)


if __name__ == '__main__':
    Q = int(input())
    solution()