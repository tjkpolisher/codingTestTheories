def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
    else:
        alphabets = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for c in list(s):
            if c in alphabets:
                answer = False
                break
    
    return answer