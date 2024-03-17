K = int(input())
for x in range(1, K + 1):  # 데이터 세트 번호를 1부터 시작하도록 변경
    n, m = map(int, input().split())
    graph = dict()
    for _ in range(m):
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:  # 양방향 관계를 고려해 B->A도 추가
            graph[b] = [a]
        else:
            graph[b].append(a)

    s = int(input())
    connected = set()
    if s in graph:
        connected = set(graph[s])  # 직접적인 친구들을 추가

    # 친구 목록을 오름차순으로 정렬해 출력
    print(f"Data Set {x}:")
    print(' '.join(map(str, sorted(connected))))
    print()  # 데이터 세트 사이에 빈 줄 추가
