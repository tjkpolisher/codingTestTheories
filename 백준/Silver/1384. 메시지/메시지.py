from collections import deque
import sys
input = sys.stdin.readline
group_num = 1

while True:
    n = int(input())

    if n == 0:
        break

    print(f"Group {group_num}")

    names_paper = dict()
    for _ in range(n):
        name_paper = list(input().split())
        name, paper_list = name_paper[0], name_paper[1:]
        names_paper[name] = paper_list

    names = names_paper.keys()
    q = deque(names)
    papers = []
    for name in names:
        if 'N' not in names_paper[name]:
            pass
        else:
            idx = []
            for i, p in enumerate(names_paper[name]):
                if p == 'N':
                    idx.append(i)
            for i in idx:
                blamer = q[-(i + 1)]
                print(f"{blamer} was nasty about {name}")
        papers += names_paper[name]
        last = q.popleft()
        q.append(last)
    if 'N' not in papers:
        print("Nobody was nasty")
    print('\n', end='')
    group_num += 1