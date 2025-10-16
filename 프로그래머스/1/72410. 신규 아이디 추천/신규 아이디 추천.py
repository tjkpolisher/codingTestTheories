def solution(new_id):
    answer = []
    # 1. 소문자 치환
    new_id = new_id.lower()
    
    # 2. 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
    for i, ch in enumerate(new_id):
        if 97 <= ord(ch) <= 122 or ch in ('0', '1', '2', '3', '4','5', '6', '7', '8', '9', '-', '_', '.'):
            # 3. 마침표가 2번 이상이면 하나만 넣기
            if answer and ch == '.' and answer[-1] == '.':
                continue
            answer.append(ch)
        
    # 4. 마침표가 처음이나 끝에 위치하면 제거
    answer = ''.join(answer)
    answer = answer.strip('.')
    
    # 5. 빈 문자열이면 "a"를 대입
    if not answer:
        answer = "a"
    
    # 6. 길이가 16자 이상이면 15개까지만 끊고, 마침표가 맨 뒤라면 제거.
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:14]
    
    # 7. 길이가 2자 이하라면, 길이가 3이 될 때까지 마지막 문자 덧붙이기
    if len(answer) <= 2:
        while len(answer) < 3:
            answer = answer + answer[-1]
    
    return answer