def solution(jobs):
    import heapq
    answer = 0  # 작업의 요청부터 종료까지 소요된 총 시간
    now = 0  # 현재 시점
    solved_task = 0  # 현재까지 처리한 job의 개수
    start = -1  # 시작 시점(먼저 힙을 최소 힙으로 만들어야 하므로 -1로 초기화)
    q = []  # 힙 초기화

    while solved_task < len(jobs):
        for job in jobs:
            # 주어진 jobs를 최소 힙으로 만들기 위한 작업
            if start < job[0] <= now:
                heapq.heappush(q, [job[1], job[0]])

        if q:
            current = heapq.heappop(q)  # 현재 수행하는 job
            start = now  # 시작 시점을 현재 시점의 시각으로 갱신
            now += current[0]  # 작업 요청 시점의 시각을 더해줌
            answer += (now - current[1])  # 이번 작업에 소모된 시간을 더해줌
            solved_task += 1
        else:
            now += 1

    return int(answer / len(jobs))