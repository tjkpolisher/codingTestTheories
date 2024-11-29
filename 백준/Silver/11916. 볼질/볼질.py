N = int(input())
balls = list(map(int, input().split()))

bases = {1: False, 2: False, 3: False}  # 시작할 때는 모든 베이스가 비어있음
score = 0  # 총 실점
ball_count = 0  # 볼의 개수, 4개가 되면 볼넷으로 타자가 출루 및 주자가 조건을 충족하면 한 베이스 진루


def forward():
    global bases, score
    if bases[3]:
        if bases[1] and bases[2]:
            bases[3] = False
            score += 1
    if bases[2]:
        if bases[1]:
            bases[2] = False
            bases[3] = True
    if bases[1]:
        bases[1] = False
        bases[2] = True
    bases[1] = True


def wild_pitch():
    global bases, score
    if bases[3]:
        bases[3] = False
        score += 1
    if bases[2]:
        bases[2] = False
        bases[3] = True
    if bases[1]:
        bases[1] = False
        bases[2] = True


for ball in balls:
    if ball == 1:
        # 볼 - 타자는 4볼일 경우 출루
        ball_count += 1
        if ball_count == 4:
            forward()
            ball_count = 0
    elif ball == 2:
        # 몸에 맞는 공 (데드볼, hit-by-pitch) - 타자 출루 및 볼 카운트 즉시 초기화
        forward()
        ball_count = 0
    elif ball == 3:
        # 폭투 - 주자 한 베이스씩 진루, 타자는 4볼이 될 때만 출루 가능
        wild_pitch()
        ball_count += 1
        if ball_count == 4:
            forward()
            ball_count = 0

print(score)