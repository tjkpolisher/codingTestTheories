def solution(a, b, n):
    # a: 콜라를 돌려주는 빈 병의 개수
    # b: 돌려받는 콜라의 개수
    # n: 빈 병의 초기 개수
    answer = 0 # 돌려받는 총 콜라의 병 수
    while True:
        q, r = divmod(n, a) # 몫: 이번 회차에서 돌려받을 콜라, 나머지: 돌려주지 못하고 남은 빈 병 개수
        if q == 0:
            break
        answer += b * q
        n = r + b * q
    return answer