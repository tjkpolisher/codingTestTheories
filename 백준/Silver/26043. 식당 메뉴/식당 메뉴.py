from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A, B, C = [], [], []  # 세 종류의 학생 목록
q = deque()
for _ in range(n):
    s = input().rstrip()
    # 유형 1의 정보가 들어올 때
    if s.startswith("1"):
        i, a, b = s.split()
        a = int(a)
        b = int(b)
        q.append([a, b])
    # 유형 2의 정보가 들어올 때
    else:
        i, b = s.split()
        b = int(b)
        student_info = q.popleft()  # 줄 맨 앞에 있는 학생 정보 pop
        if student_info[1] == b:
            A.append(student_info[0])
        else:
            B.append(student_info[0])

# 모든 s가 입력되었다면 q에 남은 인원은 모두 식사를 하지 못하므로 C에 번호 입력
while q:
    student_info = q.popleft()
    C.append(student_info[0])

A.sort()
B.sort()
C.sort()

for name_list in [A, B, C]:
    if not name_list:
        print("None")
    else:
        print(*name_list)