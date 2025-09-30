from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0  # 트럭이 다리를 건너는 시간
    net_weight = 0  # 다리 위의 트럭의 총 무게
    on_bridge = deque([0] * bridge_length)  # 다리 칸에 할당된 무게(0은 트럭이 지나지 않는 상태의 칸을 의미)
    truck_weights = deque(truck_weights)  # 트럭 무게 리스트를 큐로 변환
    
    while truck_weights:
        answer += 1
        last = on_bridge.popleft()  # 다리 위의 맨 왼쪽 원소 빼내기
        net_weight -= last
        
        # 더 이상 지나갈 트럭이 없을 경우
        if not truck_weights:
            on_bridge.append(0)
        # 현재 무게가 weight 이상일 경우
        elif net_weight + truck_weights[0] > weight:
            on_bridge.append(0)
        else:
            truck = truck_weights.popleft()  # 다리를 지나갈 트럭
            net_weight += truck
            on_bridge.append(truck)
    
    while net_weight > 0:
        answer += 1
        popped = on_bridge.popleft()
        net_weight -= popped
        
    
    return answer