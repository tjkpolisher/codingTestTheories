import sys
input = sys.stdin.readline

t = int(input())  # 테스트 케이스의 개수
for _ in range(t):
    n = int(input())  # 의상의 개수
    clothes = {}  # 의상의 종류를 키로 사용하는 딕셔너리
    for _ in range(n):
        name, kind = input().rstrip().split()  # 의상의 이름과 종류
        if kind in clothes:
            clothes[kind].append(name)
        else:
            clothes[kind] = [name]

    result = 1
    for key in clothes.keys():
        result *= (len(clothes[key]) + 1)  # 해당 의상 종류의 의상 개수

    print(result - 1)  # 알몸인 경우를 제외