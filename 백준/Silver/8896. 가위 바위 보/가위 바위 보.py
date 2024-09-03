from collections import defaultdict, deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())  # 참여하는 로봇의 수
    robots = defaultdict(deque)
    for i in range(N):
        rsp = deque(input().rstrip())
        robots[i] = rsp

    k = len(rsp)  # 문자열의 길이
    for i in range(k):
        # 로봇이 한 개만 남았으면 더 이상 게임을 하지 않아도 되므로 정지
        if len(robots) <= 1:
            break

        popped = defaultdict(str)
        # 생존한 로봇의 수만큼 가위바위보 문자열을 추출
        for j in robots.keys():
            popped[j] = robots[j].popleft()

        # 전부 똑같은 걸 내거나 다 다른 걸 냈으면 비김
        if len(set(popped.values())) == 3 or len(set(popped.values())) == 1:
            continue

        # 패배한 로봇들의 번호를 저장
        losers = set()
        if 'R' in popped.values() and 'S' in popped.values():
            for key, value in popped.items():
                if value == 'S':
                    losers.add(key)
        elif 'S' in popped.values() and 'P' in popped.values():
            for key, value in popped.items():
                if value == 'P':
                    losers.add(key)
        elif 'P' in popped.values() and 'R' in popped.values():
            for key, value in popped.items():
                if value == 'R':
                    losers.add(key)

        # 패배한 로봇 삭제
        for loser in losers:
            del robots[loser]

    if len(robots) > 1:
        print(0)
    else:
        print(list(robots.keys())[0] + 1)