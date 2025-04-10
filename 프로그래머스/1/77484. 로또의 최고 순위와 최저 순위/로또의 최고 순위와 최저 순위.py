def solution(lottos, win_nums):
    """
    lottos: 민우가 구매한 로또 번호 (0은 알아볼 수 없는 번호를 의미)
    win_nums: 실제 당첨 번호
    """
    answer = []
    if set(lottos) == set(win_nums):
        return [1, 1]
    
    # lottos에서 0 제거
    cnt = lottos.count(0)
    lottos.sort(reverse=True)
    for _ in range(cnt):
        lottos.pop()
    
    
    # Case 1. 최저 순위 번호
    # 알아볼 수 없는 번호가 전부 일치하지 않는 경우
    # 두 번호를 집합으로 바꿔서 교집합만 취함
    inter = set(lottos).intersection(set(win_nums))  # 공통되는 번호
    answer.append(min(7 - len(inter), 6))  # 일치 개수를 바탕으로 순위 책정
    
    # Case 2. 최고 순위 번호
    # 알아볼 수 있는 번호가 전부 일치하는 경우
    # win_nums 중 교집합을 제외한 부분을 lottos에서 0을 제외한 부분과 합치기
    maximum_len = cnt + len(inter)
    answer.append(min(7 - maximum_len, 6))
    
    return sorted(answer)