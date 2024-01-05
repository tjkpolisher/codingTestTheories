def solution(n):
    n3 = str(convert(n, 3))
    answer = 0
    for i in range(len(n3)):
        answer += int(n3[i]) * (3 ** i)
    return answer

def convert(num, base):
    import string
    number = string.digits + string.ascii_uppercase
    q, r = divmod(num, base)
    return convert(q, base) + number[r] if q else number[r]