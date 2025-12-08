def solution(storey):
    answer = 0
    
    while storey > 0:
        digit = storey % 10  # 현재 자릿수
        
        if digit < 5:
            # 현재 자릿수가 5보다 작으면 내림 (빼기)
            answer += digit
            storey //= 10
        elif digit > 5:
            # 현재 자릿수가 5보다 크면 올림 (더하기)
            answer += (10 - digit)
            storey = storey // 10 + 1
        else:  # digit == 5
            # 5인 경우 다음 자릿수를 확인
            next_digit = (storey // 10) % 10
            if next_digit >= 5:
                # 다음 자릿수가 5 이상이면 올림이 유리
                answer += 5
                storey = storey // 10 + 1
            else:
                # 다음 자릿수가 5 미만이면 내림이 유리
                answer += 5
                storey //= 10
    
    return answer