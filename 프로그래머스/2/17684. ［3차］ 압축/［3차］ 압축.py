def solution(msg):
    answer = []
    dictionary = {chr(65 + i): i + 1 for i in range(26)}
    next_idx = 27
    
    i = 0
    while i < len(msg):
        w = ""
        j = i  # 가장 긴 매칭 문자열 길이
        
        while j < len(msg):
            current_str = msg[i:j + 1]
            # 연장된 문자열이 딕셔너리에 있을 경우, 새로운 w로 지정
            if current_str in dictionary:
                w = current_str
                j += 1
            else:
                break
        
        answer.append(dictionary[w])
        
        if j < len(msg):
            new_word = msg[i:j + 1]
            dictionary[new_word] = next_idx
            next_idx += 1
        
        i += len(w)
    
    return answer