def solution(my_str, n):
    len_str = len(my_str)
    turn = len_str // n
    answer = []
    for i in range(turn+1):
        if i == turn:
            answer.append(my_str[n*i:])
        else:
            answer.append(my_str[n*i:n*(i+1)])
    answer = [word for word in answer if len(word)>0]
    
    return answer