def solution(n):
    bin_n = bin(n)
    cnt = bin_n.count('1')
    while True:
        n += 1
        if bin(n).count('1') == cnt:
            break
    return n