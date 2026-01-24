def summation(r):
    # 초항 3, 공비 3인 등비수열의 합
    return int(3 * (3 ** r - 1) / 2)

def solution(n):
    # 편의상, 124 나라의 수 규칙을 124진법이라고 부름
    if n == 1 or n == 2:
        return str(n)
    elif n == 3:
        return "4"
    
    # 지수 = 124진법의 자릿수
    # 1. 정지할 지수 범위
    r = 1
    while summation(r) <= n:
        r += 1
    
    # r자리 수의 시작점과의 차이
    start = summation(r - 1) + 1
    diff = n - start
    
    # diff를 3진법으로 변환
    result = []
    for i in range(r):
        result.append(diff % 3)
        diff //= 3
    
    # 역순으로 변환 후 ['1', '2', '4']로 매핑
    numbers = ['1', '2', '4']
    answer = ''.join([numbers[digit] for digit in reversed(result)])
    
    return answer