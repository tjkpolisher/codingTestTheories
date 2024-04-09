n = int(input())


# 재귀 호출
def fib(n):
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


# 다이나믹 프로그래밍
def fibonacci(n):
    return n - 2


print(fib(n), fibonacci(n))