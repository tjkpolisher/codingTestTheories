import sys
input = sys.stdin.readline

clock = [
    [["#", "#", "#"], ["#", ".", "#"], ["#", ".", "#"], ["#", ".", "#"], ["#", "#", "#"]],  # 0
    [[".", ".", "#"], [".", ".", "#"], [".", ".", "#"], [".", ".", "#"], [".", ".", "#"]],  # 1
    [["#", "#", "#"], [".", ".", "#"], ["#", "#", "#"], ["#", ".", "."], ["#", "#", "#"]],  # 2
    [["#", "#", "#"], [".", ".", "#"], ["#", "#", "#"], [".", ".", "#"], ["#", "#", "#"]],  # 3
    [["#", ".", "#"], ["#", ".", "#"], ["#", "#", "#"], [".", ".", "#"], [".", ".", "#"]],  # 4
    [["#", "#", "#"], ["#", ".", "."], ["#", "#", "#"], [".", ".", "#"], ["#", "#", "#"]],  # 5
    [["#", "#", "#"], ["#", ".", "."], ["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"]],  # 6
    [["#", "#", "#"], [".", ".", "#"], [".", ".", "#"], [".", ".", "#"], [".", ".", "#"]],  # 7
    [["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"]],  # 8
    [["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"], [".", ".", "#"], [".", ".", "#"]],  # 9
]
clock_table = {i: clock[i] for i in range(10)}

n1, n2, n3, n4 = [], [], [], []
for _ in range(5):
    n1_, n2_, n3_, n4_ = input().rstrip().split()
    n1.append(list(n1_))
    n2.append(list(n2_))
    n3.append(list(n3_))
    n4.append(list(n4_))

times = []
for i, n in enumerate([n1, n2, n3, n4]):
    if i == 0:
        clock_list = clock[:3]
    elif i == 2:
        clock_list = clock[:6]
    else:
        clock_list = clock

    counters = []
    for j, c in enumerate(clock_list):
        cnt = 0
        # 5행 3열을 순회하면서 다른 문자 체크
        for row in range(5):
            for col in range(3):
                if n[row][col] == '#' and c[row][col] == '.':
                    cnt += 1
        if cnt == 0:
            times.append(j)
            break
        else:
            counters.append(cnt)
    else:
        min_cnt = min(counters)
        times.append(counters.index(min_cnt))

print(f"{times[0]}{times[1]}:{times[2]}{times[3]}")