import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())

    l -= 1
    r -= 1
    max_score = 0

    # 접는 위치 i는 l과 r 사이, i와 i+1 사이에서 접음
    for i in range(l, r):
        # 왼쪽 절반 길이 = i-l+1, 오른쪽 절반 길이 = r-i
        overlap = min(i - l + 1, r - i)
        score = 0
        # k번쨰 매칭: S[i-k] vs S[i+1+k]
        for k in range(overlap):
            if S[i - k] == S[i + 1 + k]:
                score += 1
        if score > max_score:
            max_score = score

    print(max_score)