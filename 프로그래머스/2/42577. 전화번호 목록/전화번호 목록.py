def solution(phone_book):
    phone_book.sort()
    for i, number in enumerate(phone_book):
        if i == 0:
            continue
        if number.startswith(phone_book[i - 1]):
            return False
    
    return True