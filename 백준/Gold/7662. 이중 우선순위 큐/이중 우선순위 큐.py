from heapq import heappop, heappush
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_Q = []
    max_Q = []
    is_deleted = [True] * k
    for i in range(k):
        operation = input().rstrip()
        op, num = operation.split()
        num = int(num)
        if operation.startswith('I'):
            # 삽입 연산
            heappush(min_Q, (num, i))
            heappush(max_Q, (-num, i))
            is_deleted[i] = False
        else:
            if num == 1:
                # 최대 힙
                # 삭제되지 않은 값을 찾고, 삭제된 값을 힙에서 제거
                while max_Q and is_deleted[max_Q[0][1]]:
                    heappop(max_Q)
                if max_Q:
                    is_deleted[max_Q[0][1]] = True
                    heappop(max_Q)
            else:
                # 최소 힙
                while min_Q and is_deleted[min_Q[0][1]]:
                    heappop(min_Q)
                if min_Q:
                    is_deleted[min_Q[0][1]] = True
                    heappop(min_Q)

    # 연산이 끝난 후 삭제된 값들을 각각 최소 힙과 최대 힙에서 제거
    while max_Q and is_deleted[max_Q[0][1]]:
        heappop(max_Q)
    while min_Q and is_deleted[min_Q[0][1]]:
        heappop(min_Q)

    # 테스트 케이스에 대한 정답 출력
    if not min_Q:
        print("EMPTY")
    else:
        print(-max_Q[0][0], min_Q[0][0])