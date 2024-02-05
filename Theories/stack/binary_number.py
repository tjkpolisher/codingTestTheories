def solution(decimal):
    # 10진수를 2진수로 변환하기
    stack = []
    while decimal:
        stack.append(str(decimal % 2))
        decimal //= 2
    binary = ''.join(stack[::-1]) # 스택의 기능을 활용하면 pop()을 사용해야겠지만, join() 메서드를 사용해 시간 복잡도를 낮춘 것입니다.
    return binary

if __name__ == "__main__":
    ex1 = 10
    ex2 = 27
    ex3 = 12345
    for e in [ex1, ex2, ex3]:
        print(solution(e))