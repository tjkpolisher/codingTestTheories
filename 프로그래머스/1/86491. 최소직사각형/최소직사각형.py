def solution(sizes):
    hor, ver = [], []
    for size in sizes:
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0]
        hor.append(size[0])
        ver.append(size[1])
    max_hor, max_ver = max(hor), max(ver)
    
    
    answer = max_hor * max_ver
    return answer