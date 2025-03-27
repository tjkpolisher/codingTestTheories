import sys
from itertools import combinations
input = sys.stdin.readline

K = int(input())

for i in range(1, K + 1):
    M, N = map(int, input().split())

    table = {}
    for j in range(N):
        algorithms = list(map(int, input().split()))
        table[chr(65 + j)] = algorithms

    flag = False
    for j in range(1, M + 1):
        # 전체 원소 중 1개 ~ M개를 선택하는 조합을 시도
        if flag:
            break
        combs = combinations(table.keys(), j)
        for comb in combs:
            temp = set()  # 새 조합을 시도할 때마다 집합을 초기화
            for k in comb:
                if flag:
                    break
                for comp in table[k]:
                    temp.add(comp)
            if len(temp) == M:
                answer = list(comb)
                flag = True
                break

    # 결과 출력 단계
    print(f"Data Set {i}: {' '.join(answer)}")
    if i < K:
        print()  # 각 테스트 케이스의 사이에 빈 줄을 하나 출력