def solution(n, a, b):
    # 문제 출처: 2017 팁스타운 - 예상 대진표
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12985
    answer = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1
    return answer


if __name__ == "__main__":
    N = 8
    A = 4
    B = 7
    print(solution(N, A, B))
