def solution(my_string):
    import re
    p = re.compile('[0-9]+')
    my_string = p.findall(my_string)
    my_num = [int(num) for num in my_string]
    answer = sum(my_num)
    return answer