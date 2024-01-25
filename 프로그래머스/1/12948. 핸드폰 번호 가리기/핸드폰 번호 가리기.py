def solution(phone_number):
    length = len(phone_number)
    not_blocked = phone_number[-4:]
    answer = '*' * (length - 4) + not_blocked
    return answer