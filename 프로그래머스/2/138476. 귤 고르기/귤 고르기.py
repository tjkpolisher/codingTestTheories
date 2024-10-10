from collections import Counter
def solution(k, tangerine):  # 팔려고 하는 귤의 개수, 귤의 크기를 담은 배열
    cnt = Counter()
    for t in tangerine:
        cnt[t] += 1
    items = list(cnt.items())
    items.sort(key=lambda x: -x[1])
    
    ans = 0
    for i in range(len(items)):
        ans += 1
        k -= items[i][1]
        if k <= 0:
            break

    return ans