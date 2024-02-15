def solution(want, number, discount):
    want_table = {want[i] : number[i] for i in range(len(want))}
    cnt = 0
    
    for i in range(len(discount) - 9):
        dc_sliced = discount[i:i+10]
        dc_table = {dc_sliced[j] : dc_sliced.count(dc_sliced[j]) for j in range(len(dc_sliced))}
        if dc_table == want_table:
            cnt += 1
    
    return cnt