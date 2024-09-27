import sys
input = sys.stdin.readline

M, N = map(int, input().split())
b1, b2, b3, b4, b5 = 0, 0, 0, 0, 0  # 각 블라인드 유형의 개수
blinds = [0] * N  # 한 층의 각 창문의 블라인드 개수를 저장할 리스트

for i in range(1, 5 * M + 2):
    building = input().rstrip()
    if i % 5 == 1:
        # 1, 6, 11, ...번째 줄은 전부 창틀이므로 continue
        if i > 1:
            b1 += blinds.count(0)
            b2 += blinds.count(1)
            b3 += blinds.count(2)
            b4 += blinds.count(3)
            b5 += blinds.count(4)
            blinds = [0] * N
        continue

    for j in range(N + 1):
        if j < N and building[5 * j + 1] == '*':
            # 한 행에서 블라인드가 처진 모든 행은 '*'이므로 각 창문의 첫 글자만 '*'인지 확인
            blinds[j] += 1

print(b1, b2, b3, b4, b5)