def solution(array):
    answer = 0
    for integer in array:
        num_array = [int(i) for i in list(str(integer))]
        for num in num_array:
            if num == 7:
                answer += 1
    
    return answer