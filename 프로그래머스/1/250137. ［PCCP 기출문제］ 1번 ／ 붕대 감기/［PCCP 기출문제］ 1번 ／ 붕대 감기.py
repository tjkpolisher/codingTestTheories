def solution(bandage, health, attacks):
    # bandage: 길이 3의 정수 배열. 시전 시간 t, 초당 회복량 x, 추가 회복량 y.
    # health: 최대 체력
    # attacks: 길이 2의 정수 배열. 공격 시점 t_attack, 피해량 damage.
    
    answer = health  # 모든 공격이 끝난 후 남은 체력(초기값은 최대 체력)
    success_time = 0  # 붕대감기의 연속 성공 시간
    previous_attack = 0  # 직전 공격의 시간 (초기값은 0으로 취급)
    t, x, y = bandage  # 붕대감기의 시전 시간 t, 초당 회복량 x, 추가 회복량 y
    
    # 공격 행렬을 순회
    for attack in attacks:
        t_attack, damage = attack
        success_time = max(t_attack - previous_attack - 1, 0)  # 붕대감기의 연속 성공 시간
        
        # 공격받기 전까지의 체력 회복량 검정
        answer += x * success_time
        if success_time >= t:  # 시전 시간을 다 채우면 추가 회복
            answer += y * (success_time // t)
        answer = min(health, answer)  # 체력은 최대 체력 health를 넘을 수 없음
        
        # 공격 데미지 계산
        answer -= damage
        # 체력이 0 이하가 되어 죽으면 -1을 return
        if answer <= 0:
            return -1
        
        
        
        
        previous_attack = t_attack  # 직전 공격 시간 갱신
        print(f"{t_attack}초, 성공 시간 {success_time}, 체력 {answer}")
    
    return answer