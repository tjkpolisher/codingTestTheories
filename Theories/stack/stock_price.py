def solution(prices):
    # 문제 출처: 프로그래머스 스택/큐
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/42584
    n = len(prices)
    answer = [0] * n # 가격이 떨어지지 않은 기간을 저장할 배열
    
    # 스택을 사용해 이전 가격과 현재 가격 비교
    stack = [0] # 스택 초기화(코드 길이를 줄이기 위해 선언과 동시에 0을 넣음)
    
    ## 주의: 스택에 푸시하는 값은 주식의 가격이 아닌 인덱스입니다.
    ## 이 문제에서 최종적으로 구하는 값은 가격이 떨어지지 않은 '기간'이기 때문입니다.
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            # 가격이 떨어지면 이전 가격의 기간 계산
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    # 스택에 남아 있는 가격들은 가격이 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    return answer

if __name__ == "__main__":
    ex1 = [1, 2, 3, 2, 3]
    print(solution(ex1))