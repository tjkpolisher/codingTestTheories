import sys
input = sys.stdin.readline

N, M = map(int, input().split())
never_heard = set()  # 듣도 못한 사람
never_seen = set()  # 보도 못한 사람

for _ in range(N):
    never_heard.add(input().rstrip())
for _ in range(M):
    never_seen.add(input().rstrip())

# 교집합 연산
cross = never_heard.intersection(never_seen)
# 이름 순으로 정렬
cross = sorted(list(cross))
print(len(cross))
for c in cross:
    print(c)