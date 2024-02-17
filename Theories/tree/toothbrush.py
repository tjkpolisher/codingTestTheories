def solution(enroll, referral, seller, amount):
    # 문제 출처: 2021 Dev-Matching: 웹 백엔드 개발자(상반기) - 다단계 칫솔 판매
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/77486

    parent = dict(zip(enroll, referral))
    
    total = {name: 0 for name in enroll}
    
    for i in range(len(seller)):
        money = amount[i] * 100
        cur_name = seller[i]
        
        while money > 0 and cur_name != "-":
            total[cur_name] += money - money // 10
            cur_name = parent[cur_name]
            money //= 10

    answer = [total[name] for name in enroll]
    return answer


if __name__ == "__main__":
    ex1 = [["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
           ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
           ["young", "john", "tod", "emily", "mary"],
           [12, 4, 2, 5, 10]]
    ex2 = [["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
           ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
           ["sam", "emily", "jaimie", "edward"],
           [2, 3, 5, 4]]
    for e in [ex1, ex2]:
        print(solution(e[0], e[1], e[2], e[3]))
