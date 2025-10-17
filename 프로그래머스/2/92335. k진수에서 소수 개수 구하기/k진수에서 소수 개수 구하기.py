def convert(n, k):
    answer = ''
    while n >= k:
        n, mod = divmod(n, k)
        answer += str(mod)
    answer += str(n)
    return answer[::-1]

def solution(n, k):
    # n: 양의 정수(십진수 형태), k: 변환할 진수
    converted_n = convert(n, k)
    print(f"{converted_n=}")
    converted_n_list = list(converted_n.split('0'))
    
    answer = 0
    converted_n_list = [int(i) for i in converted_n_list if i != '']
    for number in converted_n_list:
        if number == 1:
            continue
        if number in (2, 3):
            answer += 1
            continue
        answer += 1
        for j in range(2, int(number ** 0.5) + 1):
            if number % j == 0:
                answer -= 1;
                break
    return answer