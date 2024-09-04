def solution(s):
    s = s[2:-2].split("},{")
    s.sort(key=len)
    
    answer = []
    for element in s:
        numbers = element.split(",")
        for number in numbers:
            if int(number) not in answer:
                answer.append(int(number))
    return answer