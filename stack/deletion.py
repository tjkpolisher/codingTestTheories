def solution(s):
    # 문제 출처: 2017 팁스타운 - 짝지어 제거하기
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12973
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            # 스택이 비어있지 않고, 현재 문자와 스택 맨 위의 문자가 같을 경우
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        return 1
    else:
        return 0

if __name__ == "__main__":
    ex1 = "baabaa"
    ex2 = "cdcd"
    for e in [ex1, ex2]:
        print(solution(e))