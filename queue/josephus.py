def solution(n, k):
    # 연관 문제: 백준 1158(요세푸스 문제)(https://www.acmicpc.net/problem/1158)
    # 문제 포인트: 요세푸스 문제를 그림으로 나타날 때는 보통 원형으로 사람을 배치합니다.
    # 이 때문에 "원형 큐를 이용해야 하지 않나?"하는 의문이 들 수도 있습니다.
    # 하지만 코딩 테스트에서는 리스트를 사용해도 메모리를 크게 낭비하지 않으므로 선형 큐를 사용해도 충분합니다.
    from collections import deque
    dq = deque(range(1, N + 1))
    
    while len(dq) > 1: # dq에 요소가 하나만 남을 때까지 실행
        for _ in range(K - 1):  # K번째 요소를 찾기 위해 앞에서부터 제거하고 뒤에 추가
            dq.append(dq.popleft())
        
        dq.popleft() # K번째 요소 제거
    
    return dq[0]

if __name__ == "__main__":
    N, K = 5, 2
    print(solution(N, K))
    
# 추가 주석
# 이 문제는 세그먼트 트리 자료구조를 사용해 풀면 시간 복잡도를 O(NlogN)으로 개선할 수 있습니다.