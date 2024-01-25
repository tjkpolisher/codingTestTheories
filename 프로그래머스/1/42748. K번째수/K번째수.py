def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        sliced = array[i - 1:j]
        sliced = sorted(sliced)
        answer.append(sliced[k-1])
    return answer