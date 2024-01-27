def solution(s):
    # 문제 출처: 프로그래머스 월간 코드 챌린지 - 괄호 회전하기
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/76502
    answer = 0
    n = len(s)
    for i in range(n):
        stack = []
        for j in range(n):
            # 괄호 문자열을 회전시키면서 참조
            ## 문자열을 진짜로 회전시키면 연산 비용이 많이 들기 때문에, 대신 인덱스를 활용합니다.
            c = s[(i + j) % n]
            if c == "(" or c == "{" or c =="[": # 열린 괄호 푸시
                stack.append(c)
            else:
                if not stack: # 짝이 맞지 않는 경우
                    break
            
                # 닫힌 괄호는 스택의 top과 짝이 맞는지 비교
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    break
                
        else: # for 문이 break에 의해 끝나지 않고 끝까지 수행된 경우
            ## for-else문: for문이 끝까지 실행되었을 때에만 동작합니다.
            if not stack:
                answer += 1
    return answer

if __name__ == "__main__":
    ex1 = "[](){}"
    ex2 = "}]()[{"
    ex3 = "[)(]"
    ex4 = "}}}"
    for e in [ex1, ex2, ex3, ex4]:
        print(solution(e))