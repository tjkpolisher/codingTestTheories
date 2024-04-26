from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
words = dict()
cnt = 0
for i in range(N):
    word = input().rstrip()

    if i == 0 or len(word) not in words:
        cnt += 1
        words[len(word)] = [word]
        continue
    else:      
        q = deque(word)
        is_same = False
        words_to_compare = words[len(word)]
        for w in words_to_compare:
            for _ in range(len(word)):
                p = q.popleft()
                q.append(p)
                is_same = (w == ''.join(q))
                # 어느 한 단어와도 동일했을 경우 정지
                if is_same:
                    break
            if is_same:
                break
        # 길이가 같은 모든 단어와 비교해도 다른 단어일 때
        # 비교할 단어 리스트를 전부 순회했을 때만 기능하는 절입니다.
        else:
            cnt += 1
            words[len(word)].append(word)

print(cnt)