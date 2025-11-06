def solution(numbers):
    answer = []
    
    def f(x):
        """
        x보다 크고 x와 비트가 1~2개 다른 수들 중 제일 작은 수를 구하는 함수
        """
        # 짝수인 경우: 맨 끝 비트만 1로 바꾸면 됨
        if x % 2 == 0:
            return x + 1
        
        # 홀수인 경우: 오른쪽부터 첫 번째 0을 찾아서 처리
        binary_x = '0' + bin(x)[2:]  # 맨 앞에 0 추가 (모든 비트가 1인 경우 대비)
        binary_list = list(binary_x)
        
        # 오른쪽부터 첫 번째 0의 위치 찾기
        for i in range(len(binary_list) - 1, -1, -1):
            if binary_list[i] == '0':
                # 그 0을 1로 바꾸고, 바로 오른쪽 비트를 0으로 바꿈
                binary_list[i] = '1'
                binary_list[i + 1] = '0'
                return int(''.join(binary_list), 2)

    for number in numbers:
        answer.append(f(number))
    
    return answer