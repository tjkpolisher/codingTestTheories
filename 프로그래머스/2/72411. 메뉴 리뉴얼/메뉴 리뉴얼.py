from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    # 1. 코스 요리의 요리 개수 별로 수행
    for size in course:
        tmp = []
        # 2. 모든 주문에 대해 해당 사이즈의 조합을 만들기
        for order in orders:
            order_list = sorted(order)
            
            combs = combinations(order_list, size)
            tmp.extend(combs)
        
        # 3. 생성된 모든 조합의 개수 count
        counter = Counter(tmp)
        
        # 4. 가장 많이 주문된 횟수 찾기
        if counter:
            max_cnt = counter.most_common(1)[0][1]
            # 5. 최소 2명 이상 주문 + 최빈값과 횟수가 같은 경우만 더하기
            if max_cnt >= 2:
                for key, value in counter.items():
                    if value == max_cnt:
                        answer.append("".join(key))
    
    return sorted(answer)