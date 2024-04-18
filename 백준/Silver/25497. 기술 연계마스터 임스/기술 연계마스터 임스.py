import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
skills = deque(input().rstrip())
cnt = 0
stack_L = []  # 사전 기술 L을 담을 스택
stack_S = []  # 사전 기술 S를 담을 스택

for i in range(N):
    p = skills.popleft()
    # L 또는 S인 경우 본 기술이 나오기 전까지 별도의 스택에 저장
    if p == 'L':
        stack_L.append(p)
    elif p == 'S':
        stack_S.append(p)
    # R인 경우 stack_L에 L이 있는 경우 스택에서 L을 빼고 카운터 증가
    elif p == 'R':
        if not stack_L:
            break
        else:
            stack_L.pop()
            cnt += 1
    # K인 경우 stack_S에 S이 있는 경우 스택에서 S을 빼고 카운터 증가
    elif p == 'K':
        if not stack_S:
            break
        else:
            stack_S.pop()
            cnt += 1
    # 나머지 일반 기술들의 경우 그대로 카운터 증가
    else:
        cnt += 1

print(cnt)