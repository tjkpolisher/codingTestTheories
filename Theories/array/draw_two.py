def solution(numbers):
    # 원본 출처: 프로그래머스 월간 코드 챌린지
    # https://programmers.co.kr/learn/courses/30/lessons/68644
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            summation = numbers[i] + numbers[j]
            if summation not in answer:
                answer.append(summation)
    answer.sort()
    return answer

if __name__ == '__main__':
    ex1 = [2, 1, 3, 4, 1]
    ex2 = [5, 0, 2, 7]
    for e in [ex1, ex2]:
        print(solution(e))