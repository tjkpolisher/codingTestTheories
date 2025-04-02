import re

def solution(dartResult):
    answer = 0
    last, now = 0, 0
    
    strings = re.findall("[\D]+", dartResult)
    nums = re.findall("[\d]+", dartResult)
    
    scores = {'S': 1, 'D': 2, 'T': 3, '*': 2, '#': -1}
    for n, s in zip(nums, strings):
        if len(s) == 2: 
            now = int(n) ** scores[s[0]] * scores[s[1]]
            if s[1] == '*':
                last *= 2
        else:
            now = int(n) ** scores[s]
        
        answer += last
        last, now = now, 0

    return answer + last