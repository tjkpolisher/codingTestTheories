def solution(friends, gifts):
    answer = 0  # 다음 달에 가장 많은 선물을 받는 친구가 받을 선물의 수
    num = len(friends)
    
    # 1. 필요한 2차원 리스트 및 딕셔너리 생성
    gift_table = [[0] * num for _ in range(num)]  # 선물 테이블
    friends_index = {friends[i]: i for i in range(num)}  # 친구 이름 및 번호 딕셔너리
    gift_score = {friend: 0 for friend in friends}  # 선물 지수 딕셔너리
    
    # 2. gifts를 순회하면서 선물 테이블 채우기 + 선물 지수 계산
    for gift in gifts:
        A, B = gift.split()  # 준 사람, 받는 사람
        
        # 선물 테이블 채우기
        A_idx, B_idx = friends_index[A], friends_index[B]
        gift_table[A_idx][B_idx] += 1
        
        # 선물 지수 계산
        gift_score[A] += 1  # 준 만큼 1 더하기
        gift_score[B] -= 1  # 받은 만큼 1 빼기
    
    # 3. 이름을 순회하면서 선물 정산
    for name in friends:
        tmp = 0
        name_idx = friends_index[name]
        for friend in friends:
            if name == friend:  # 같은 이름이면 비교하지 않음
                continue
            friend_idx = friends_index[friend]
            gift1 = gift_table[name_idx][friend_idx]
            gift2 = gift_table[friend_idx][name_idx]
            if gift1 > gift2:
                tmp += 1
                continue
            if gift1 == gift2:
                if gift_score[name] > gift_score[friend]:
                    tmp += 1
        answer = max(answer, tmp)
        
    return answer