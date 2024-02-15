def solution(participant, completion):
    complete_table = {}
    
    for p in participant:
        if p in complete_table:
            complete_table[p] += 1
        else:
            complete_table[p] = 1
    
    for c in completion:
        complete_table[c] -= 1
    
    for key in complete_table.keys():
        if complete_table[key] > 0:
            return key