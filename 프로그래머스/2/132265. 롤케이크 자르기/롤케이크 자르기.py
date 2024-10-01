from collections import Counter

def solution(topping):
    answer = 0
    cnt = Counter(topping)
    roll = set()
    
    for i in topping:
        cnt[i] -= 1
        roll.add(i)
        if cnt[i] == 0:
            cnt.pop(i)
        if len(cnt) == len(roll):
            answer += 1
    
    return answer