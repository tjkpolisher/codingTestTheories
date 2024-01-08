def solution(s, n):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets_upper = alphabets.upper()
    s_list = list(s)
    
    for i, c in enumerate(s_list):
        if c.isupper():
            idx = alphabets_upper.index(c) + n
            if idx >= 25:
                idx -= 26
            new_c = alphabets_upper[idx]
            s_list[i] = new_c
        elif c.islower():
            idx = alphabets.index(c) + n
            if idx >= 25:
                idx -= 26
            new_c = alphabets[idx]
            s_list[i] = new_c
    
    answer = ''.join(s_list)
    
    return answer