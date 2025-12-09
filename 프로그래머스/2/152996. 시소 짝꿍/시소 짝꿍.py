from collections import Counter
def solution(weights):
    answer = 0
    distances = [2, 3, 4]
    
    # 무게별 개수 카운트
    weight_count = Counter(weights)
    unique_weights = sorted(set(weights))
    
    for i, weight in enumerate(unique_weights):
        count = weight_count[weight]
        
        # 같은 무게끼리 짝을 이루는 경우 (같은 거리에 앉음)
        if count >= 2:
            answer += count * (count - 1) // 2
        
        # 다른 무게와 짝을 이루는 경우
        for d1 in distances:
            torque1 = weight * d1  # 왼쪽 탑승자에 몸무게에 의한 토크 1
            
            for j in range(i + 1, len(unique_weights)):
                for d2 in distances:
                    torque2 = unique_weights[j] * d2
                    if torque1 == torque2:  # 평형을 이룰 경우
                        answer += count * weight_count[unique_weights[j]]
                        break
                    elif torque1 < torque2:  # 우측 토크가 더 클 경우 그대로 break
                        break
    
    return answer