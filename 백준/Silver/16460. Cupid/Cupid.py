import sys
input = sys.stdin.readline

p_user_info = list(input().rstrip().split())
preference = list(p_user_info[1])
max_distance = int(p_user_info[2])

N = int(input())

ans = []

for _ in range(N):
    name, sex, distance = input().rstrip().split()
    distance = int(distance)

    if sex not in preference:  # 성적 취향 체크
        continue
    if distance > max_distance:  # 최대 거리 체크
        continue
    ans.append(name)

if not ans:
    print("No one yet")
else:
    ans.sort()  # 사전 순서대로 리스트 정렬
    for name in ans:
        print(name)