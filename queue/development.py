def solution(progresses, speeds):
    # 문제 출처: 프로그래머스 스택/큐 - 기능 개발
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42586
    from math import ceil
    answer = []
    n = len(progresses)
    # 각 작업의 배포 가능일 계산
    days_left = [ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    
    count = 0
    max_day = days_left[0]
    
    for i in range(n):
        if days_left[i] <= max_day:  # 배포 가능일이 가장 늦은 배포일보다 빠를 경우
            count += 1
        else:  # 배포 가능일이 가장 늦은 배포일보다 늦을 경우
            answer.append(count)
            count = 1
            max_day = days_left[i]
    
    # 마지막 작업이 카운트되지 않기 때문에 루프 바깥에서 한 번 더 append
    answer.append(count)
    return answer


if __name__ == "__main__":
    ex1 = [[93, 30, 55], [1, 30, 5]]
    ex2 = [[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]]
    for e in [ex1, ex2]:
        print(solution(e[0], e[1]))