def solution(arr):
    minimum = min(arr)
    arr.remove(minimum)
    answer = arr
    if not answer:
        answer = [-1]
    return answer