from collections import deque
def solution(x, y, n):
    if x == y:
        return 0
    answer = 0
    
    # 1. 연산 후 결과를 담을 집합 형성(첫 번째 노드의 값은 x)
    natural_numbers = set()  # 방문한 노드들

    # 2. BFS에 사용할 큐 생성
    q = deque()
    q.append(x)
    natural_numbers.add(x)
    
    # 3. BFS 실행
    while q:
        former_length = len(natural_numbers)  # 이 단계 이전의 방문한 노드들의 개수
        current_q_length = len(q)

        for _ in range(current_q_length):
            current_node = q.popleft()
            
            # 4. 연산 진행
            results = [current_node + n, current_node * 2, current_node * 3]

            for result in results:
                # 목표 도달 시 종료
                if result == y:
                    return answer + 1
                # 연산이 범위를 넘어서면 추가하지 않음
                elif result <= y and result not in natural_numbers:
                    q.append(result)
                    natural_numbers.add(result)
        answer += 1

    # 큐가 빌 때까지 y에 도달하지 못하면 -1 반환
    return -1