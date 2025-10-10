def solution(order):
    n = len(order)
    auxiliary_belt = []  # 보조 컨테이너 벨트 (스택)
    order_idx = 0  # 현재 실어야 할 order의 인덱스

    # 메인 벨트에서 1번부터 n번 상자까지 순서대로 처리
    for box in range(1, n + 1):
        # 현재 박스가 지금 실어야 할 박스인 경우
        if box == order[order_idx]:
            order_idx += 1
            # 보조 벨트에서도 실을 수 있는지 확인
            while order_idx < n and auxiliary_belt and auxiliary_belt[-1] == order[order_idx]:
                auxiliary_belt.pop()
                order_idx += 1
        else:
            # 보조 벨트에 넣을 수 있는지 확인
            # 보조 벨트는 증가하는 순서로만 유지되어야 함
            if auxiliary_belt and auxiliary_belt[-1] >= box:
                # 더 이상 루프 진행 불가능
                break
            auxiliary_belt.append(box)
    
    # 남은 상자들을 보조 벨트에서 처리
    while order_idx < n and auxiliary_belt and auxiliary_belt[-1] == order[order_idx]:
        auxiliary_belt.pop()
        order_idx += 1
    
    return order_idx