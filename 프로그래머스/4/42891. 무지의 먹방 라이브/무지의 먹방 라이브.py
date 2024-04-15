def solution(food_times, k):
    """
    food_times: 각 음식을 모두 먹는데 필요한 시간이 음식의 번호 순서대로 들어있는 배열
    k: 방송이 중단된 시간
    ==================
    Result: 방송 재개 후 다시 먹기 시작할 음식의 번호
    (음식이 없으면 -1을 반환)
    """
    """i = 0
    n = len(food_times)  # 음식 개수
    t = 0
    zeros = food_times.count(0)  # food_times 안의 0의 개수
    while True:
        if zeros == n:
            return -1
        if i >= n:
            i = 0
        
        if food_times[i] == 0:
            i += 1
            continue
        elif t == k:
            return i + 1
        else:
            food_times[i] -= 1
            if food_times[i] == 0:
                zeros += 1
            i += 1
        
        t += 1"""
    
    import heapq
    if sum(food_times) <= k:
        return -1
    
    q = []
    sum_value = 0
    previous = 0
    length = len(food_times)
    for i in range(length):
        heapq.heappush(q, (food_times[i], i + 1))
    
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]