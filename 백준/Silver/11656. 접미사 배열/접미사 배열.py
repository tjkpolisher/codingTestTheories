from collections import deque

S = deque(input())
S_list = []
while S:
    S_list.append(''.join(S))
    S.popleft()

S_list.sort()
for word in S_list:
    print(word)