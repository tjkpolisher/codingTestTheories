import heapq
def solution(operations):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙
    visited = {}  # 유효한 값이 저장되었는지를 나타내는 딕셔너리
    
    for idx, command in enumerate(operations):
        command = command.split()
        
        if command[0] == 'I':
            # 주어진 숫자를 큐에 삽입
            num = int(command[1])
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            visited[idx] = True  # 이 값이 유효함을 딕셔너리에 저장
        elif command[0] == 'D':
            if command[1] == '1':
                # 최대값을 삭제
                while max_heap and not visited.get(max_heap[0][1], False):
                    # 유효하지 않은 값들을 삭제
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False  # 유효 처리 해제
                    heapq.heappop(max_heap)
            elif command[1] == '-1':
                # 최소값을 삭제
                while min_heap and not visited.get(min_heap[0][1], False):
                    # 유효하지 않은 값들을 삭제
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False  # 유효 처리 해제
                    heapq.heappop(min_heap)
    
    # 최종 결과 출력 전, 힙의 최상단에 있는 유효하지 않은 값들을 제거
    while min_heap and not visited.get(min_heap[0][1], False):
        heapq.heappop(min_heap)
    while max_heap and not visited.get(max_heap[0][1], False):
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        return [-max_heap[0][0], min_heap[0][0]]
    else:
        return [0, 0]