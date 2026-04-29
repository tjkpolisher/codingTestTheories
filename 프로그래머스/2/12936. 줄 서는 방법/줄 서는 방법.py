from math import factorial
def solution(n, k):
    # n = 1이면 k = 1로 강제되고 답은 [1] 뿐임
    if n == 1:
        return [1]

    answer = []
    numbers = list(range(1, n + 1))
    k -= 1
    
    def insert_number(k):
        i = 0
        interval = factorial(len(numbers) - 1)
        while True:
            if i * interval <= k < (i + 1) * interval:
                break
            i += 1
        k -= interval * i
        return i, k
    
    # answer의 원소가 n개가 될 때까지 반복
    while len(answer) < n:
        idx, k = insert_number(k)
        num = numbers[idx]
        answer.append(num)
        numbers.remove(num)
    return answer