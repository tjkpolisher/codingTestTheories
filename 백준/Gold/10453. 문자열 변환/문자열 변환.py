import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = input().rstrip().split()

    # a와 b의 개수가 서로 다르면 -1을 출력 후 다음 케이스로 진행
    counter_A = Counter(A)
    counter_B = Counter(B)
    if counter_A['a'] != counter_B['a'] and counter_A['b'] != counter_B['b']:
        print(-1)
        continue

    pos_A = [i for i, ch in enumerate(A) if ch == 'a']
    pos_B = [i for i, ch in enumerate(B) if ch == 'a']

    ans = 0
    for a_idx, b_idx in zip(pos_A, pos_B):
        ans += abs(a_idx - b_idx)
    print(ans)