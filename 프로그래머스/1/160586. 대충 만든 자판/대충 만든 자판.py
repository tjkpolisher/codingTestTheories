def solution(keymap, targets):
    answer = []
    char_min_press = {} # 각 문자의 최소 입력 횟수
    
    # keymap을 순회하면서 각 문자의 최소 입력 횟수 계산
    for key_chars in keymap:
        for char_idx, char in enumerate(key_chars):
            press_cnt = char_idx + 1
            if char not in char_min_press:
                char_min_press[char] = press_cnt
            else:
                char_min_press[char] = min(char_min_press[char], press_cnt)
    
    # 각 target 문자열에 대해 최소 입력 횟수 계산
    for target in targets:
        total = 0
        flag = True
        for char in target:
            if char not in char_min_press:
                flag = False
                break
            total += char_min_press[char]
        if flag:
            answer.append(total)
        else:
            answer.append(-1)
    
    return answer