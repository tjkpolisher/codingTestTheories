from math import gcd
from functools import reduce
def solution(arrayA, arrayB):
    answer = 0
    
    # 1. 두 배열의 최대공약수 구하기
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)
    
    # 2. 조건을 만족하는지 확인
    flag1 = True
    for num in arrayB:
        if num % gcdA == 0:
            flag1 = False
            break

    flag2 = True
    for num in arrayA:
        if num % gcdB == 0:
            flag2 = False
            break
    
    # 3. 최대값 반환
    if flag1:
        answer = max(answer, gcdA)
    if flag2:
        answer = max(answer, gcdB)
    
    return answer