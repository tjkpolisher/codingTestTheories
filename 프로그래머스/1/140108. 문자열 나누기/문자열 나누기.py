def solution(s):
    answer = []
    first = s[0]
    itIs, isNot = 0, 0
    sliced = ''
    for i in range(len(s)):
        if s[i] == first:
            itIs += 1
        else:
            isNot += 1
        
        sliced += s[i]
        
        if itIs == isNot or i == len(s) - 1:
            answer.append(sliced)
            sliced = ''
            if i < len(s) - 1:
                first = s[i+1]
        
    return len(answer)