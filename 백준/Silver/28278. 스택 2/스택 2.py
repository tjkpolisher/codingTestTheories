import sys
input = sys.stdin.readline

N = int(input())
stack = []


def pop_and_print(stack):
    if stack:
        p = stack.pop()
        print(p)
    else:
        print(-1)
    return stack


def is_empty(stack):
    # 스택이 비어있을 때 1, 아니면 0을 출력해야 하므로 True/False를 원래와 반대로 설정
    return True if not stack else False


def top(stack):
    if stack:
        print(stack[-1])
    else:
        print(-1)


for _ in range(N):
    command = input().rstrip()
    if command.startswith('1'):
        _, x = command.split()
        stack.append(int(x))
    elif command == '2':
        stack = pop_and_print(stack)
    elif command == '3':
        print(len(stack))
    elif command == '4':
        print(int(is_empty(stack)))
    else:
        top(stack)