from math import ceil
def solution(fees, records):
    """
    fees(List): 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
    records(List): "시각(HH:MM) 차량번호(길이 4 문자열) 내역('IN' 또는 'OUT')"
    """
    answer = []
    table = {}  # 차량번호 - 시각을 저장하는 딕셔너리
    
    # 1. 요금 정보 분해
    basis_time = fees[0]  # 기본 시간
    basis_fee = fees[1]  # 기본 요금
    unit_time = fees[2]  # 단위 시간
    unit_fee = fees[3]  # 단위 요금
    
    def calculate_fee(net_time, car_number):
        if net_time <= basis_time:
            answer.append((car_number, basis_fee))
        else:
            net_fee = basis_fee + ceil((net_time - basis_time) / unit_time) * unit_fee
            answer.append((car_number, net_fee))
    
    # 2. 출차 내역 조회
    for record in records:
        time, car_number, in_or_out = record.split()
        hour, minute = time.split(":")
        net_time = int(hour) * 60 + int(minute)  # 3. 시간을 분 단위로 환산
        
        # 4-1. 입차 처리
        if in_or_out == "IN":
            if car_number not in table:
                table[car_number] = [net_time]
            else:
                table[car_number].append(net_time)
        # 4-2. 출차 처리
        elif in_or_out == "OUT":
            table[car_number].append(net_time)
    
    for car_number in table.keys():
        if len(table[car_number]) % 2 == 1:  # 길이가 홀수일 경우 마지막 출차 기록이 없는 것
            table[car_number].append(23 * 60 + 59)
        net_time = 0
        for i in range(len(table[car_number]) // 2):
            net_time += (table[car_number][2 * i + 1] - table[car_number][2 * i])
        calculate_fee(net_time, car_number)
    
    # 5. 정답 리스트를 차량번호 오름차순으로 정렬
    answer.sort(key=lambda x: x[0])
            
    return [element[1] for element in answer]