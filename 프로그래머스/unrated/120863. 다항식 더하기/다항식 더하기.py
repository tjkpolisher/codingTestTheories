def solution(polynomial):
    poly = polynomial.split(' ')
    num, x_coef = [], []
    for word in poly:
        if 'x' in word:
            if len(word)==1:
                x_coef.append(int(1))
            else:
                x_coef.append(int(word[:-1]))
        elif word == '+':
            pass
        else:
            num.append(int(word))
    
    sum_num = sum(num) if num else 0 # 상수항
    sum_x_coef = sum(x_coef) if x_coef else 0 # x의 계수
    if sum_x_coef == 1:
        sum_x_coef = ''
    
    if sum_x_coef == 0:
        answer = str(sum_num)
    elif sum_num == 0:
        answer = str(sum_x_coef) + 'x'
    else:
        answer = str(sum_x_coef) + 'x + ' + str(sum_num)
    return answer