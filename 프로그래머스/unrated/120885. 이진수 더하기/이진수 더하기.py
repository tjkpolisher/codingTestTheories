def solution(bin1, bin2):
    int1, int2 = int(bin1, 2), int(bin2, 2)
    answer = bin(int1 + int2)
    return answer[2:]