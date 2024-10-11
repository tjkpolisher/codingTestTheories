from collections import deque
def solution(elements):
    sum_nums = set()
    length = len(elements)
    
    for i in range(1, length):
        q = deque(elements)
        q_temp = deque()  # 연속 부분 순열을 나타내는 덱 초기화
        while len(q_temp) < i:
            # 길이 i의 연속 부분 수열 생성
            q_temp.append(q.popleft())
        
        for j in range(length):
            sum_nums.add(sum(q_temp))
            q_temp.append(q.popleft())
            q.append(q_temp.popleft())
    
    sum_nums.add(sum(elements))
    
    return len(sum_nums)