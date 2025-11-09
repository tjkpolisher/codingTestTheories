def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2
    
    # 1. 전체 합이 홀수면 합을 같게 만들 수 없음
    if total % 2 == 1:
        return -1
    
    # 2. 원소 중 하나가 target보다 크면 불가능
    target = total // 2  # 각 큐의 합의 목표치
    if max(max(queue1), max(queue2)) > target:
        return -1
    
    # 3. 두 큐를 하나의 배열로 연결
    net_queue = queue1 + queue2
    n = len(queue1)
    
    # 4. 슬라이딩 윈도우
    left = 0
    right = n - 1  # queue1의 마지막 인덱스
    current_sum = sum1
    
    for cnt in range(3 * n + 1):
        if current_sum == target:
            return cnt
        
        if current_sum > target:
            current_sum -= net_queue[left]
            left += 1
        else:
            right += 1
            if right >= len(net_queue):
                break
            current_sum += net_queue[right]
    
    return -1