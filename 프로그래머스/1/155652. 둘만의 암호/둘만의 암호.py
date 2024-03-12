def solution(s, skip, index):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    alphabet = sorted(list(alphabet - set(skip)))
    s = list(s)
    for i, c in enumerate(s):
        idx = alphabet.index(c)
        idx += index
        
        if idx >= len(alphabet):
            while idx >= len(alphabet):
                idx -= len(alphabet)
        
        s[i] = alphabet[idx]
    
    answer = ''.join(s)
    return answer