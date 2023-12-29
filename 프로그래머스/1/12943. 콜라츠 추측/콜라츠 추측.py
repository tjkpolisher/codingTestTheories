def solution(num):
    counter = 0
    while num != 1:
        if counter > 500:
            counter = -1
            break
        elif num == 1:
            break
        else:
            if num % 2 == 0:
                num //= 2
            else:
                num = 3 * num + 1
            
            counter += 1
        
    return counter