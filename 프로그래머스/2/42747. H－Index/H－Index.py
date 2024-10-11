def solution(citations):
    citations.sort(reverse=True)
    h = 0
    for i in range(len(citations)):
        if i + 1 <= citations[i]:
            h = i + 1
    return h