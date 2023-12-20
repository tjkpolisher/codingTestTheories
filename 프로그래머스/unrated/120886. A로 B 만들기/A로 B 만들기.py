def solution(before, after):
    bef_sort = sorted(before)
    aft_sort = sorted(after)
    answer = 1 if bef_sort == aft_sort else 0
    return answer