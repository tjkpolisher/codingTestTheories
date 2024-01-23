def solution(food):
    answer = '0'
    food = food[1:]
    entry = ''
    for i, f in enumerate(food):
        entry += (f // 2) * str(i + 1)
    answer = entry + answer + entry[::-1]
    return answer