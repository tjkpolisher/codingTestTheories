def solution(priorities, location):
    from collections import deque
    priorities = deque(priorities)
    idxs = deque(range(len(priorities)))
    cnt = 0
    while True:
        max_p = max(priorities)
        p = priorities.popleft()
        idx = idxs.popleft()
        if p == max_p:
            cnt += 1
        else:
            priorities.append(p)
            idxs.append(idx)
        
        if p == max_p and idx == location:
            break
    return cnt