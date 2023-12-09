def solution(quiz):
    answer = []
    
    for quote in quiz:
        quote = list(quote)
        equal = quote.index("=")
        quote1 = ''.join(quote[:equal-1])
        quote2 = int(''.join(quote[equal+2:]))
        if eval(quote1)==quote2:
            answer.append("O")
        else:
            answer.append("X")
    
    return answer