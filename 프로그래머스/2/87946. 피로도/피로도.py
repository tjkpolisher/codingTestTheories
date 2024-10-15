from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        temp = k
        cnt = 0
        for e1, e2 in p: # 각각 필요 피로도와 소모 피로도를 의미
            if temp >= e1:
                temp -= e2
                cnt += 1
        
        answer = max(answer, cnt)
    return answer