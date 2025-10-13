def solution(sequence, k):
    i = 0  # 포인터 1
    n = len(sequence)
    current_sum = 0
    min_length = 10 ** 7  # 적당히 큰 수로 초기화
    answer = [0, 0]
    
    for j in range(n):  # 포인터 2
        current_sum += sequence[j]
        
        while current_sum > k and i <= j:
            current_sum -= sequence[i]
            i += 1
        
        if current_sum == k:
            length = j - i + 1
            if length < min_length:
                min_length = length
                answer = [i, j]
    return answer