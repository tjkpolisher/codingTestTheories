def solution(number, k):
    answer = []
    remove_count = 0
    
    for num in number:
        # 스택의 마지막 숫자가 현재 숫자보다 작고, 아직 k개를 제거하지 않았다면
        while answer and answer[-1] < num and remove_count < k:
            answer.pop()
            remove_count += 1
        
        answer.append(num)
    
    # 아직 k개를 모두 제거하지 못한 경우
    # 뒤에서부터 남은 개수만큼 제거
    if remove_count < k:
        answer = answer[:-(k - remove_count)]
    
    return ''.join(answer)