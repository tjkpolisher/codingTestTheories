import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = dict()  # 곡명과 곡명 길이, 음계를 저장할 딕셔너리

for i in range(N):
    input_string = list(input().split())
    T = input_string[0]
    S = input_string[1]
    pitches = input_string[2:]
    table[i] = [S, pitches]

for _ in range(M):
    # 알고 있는 음(known-pitches, kp)
    kp = list(input().split())
    # 첫 세 음이 kp와 동일한 곡의 제목
    matched = []
    for key in table.keys():
        name = table[key][0]
        pitch_list = table[key][1]
        # 첫 세 음이 동일하면 이름 저장
        if kp == pitch_list[:3]:
            matched.append(name)
        # 해당하는 음악이 2개 이상이면 루프 탈출
        if len(matched) >= 2:
            break

    if len(matched) >= 2:
        print("?")
    else:
        if not matched:
            print("!")
        else:
            print(matched[0])