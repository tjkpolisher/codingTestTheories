def solution(s):
    cnt = 0
    zeros = 0
    while True:
        answer = []
        for i in range(len(s)):
            if s[i] == '1':
                answer.append(s[i])
            elif s[i] == '0':
                zeros += 1
        cnt += 1
        s = bin(len(answer))[2:]
        if s == '1':
            break
    
    return [cnt, zeros]