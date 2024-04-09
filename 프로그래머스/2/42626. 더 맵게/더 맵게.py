def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)

    cnt = 0
    while scoville[0] < K:
        cnt += 1
        least1 = heapq.heappop(scoville)
        least2 = heapq.heappop(scoville)

        new_score = least1 + least2 * 2
        heapq.heappush(scoville, new_score)

        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return cnt