import heapq
def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    heap = []
    for idx in range(len(enemy)):
        # 1. 현재 적을 힙에 추가 (무적권 사용 후보)
        heapq.heappush(heap, enemy[idx])
        
        # 2. 힙 크기가 k 초과 시, 가장 적은 적을 병사로 처리
        if len(heap) > k:
            min_enemy = heapq.heappop(heap)
            n -= min_enemy
            
            # 병사 부족 시 그대로 게임 종료
            if n < 0:
                return idx
            
    # 모든 라운드 클리어 시
    return len(enemy)