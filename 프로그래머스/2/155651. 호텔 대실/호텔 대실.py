def solution(book_time):
    # 1. 대실 시작 시간 기준으로 오름차순 정렬
    book_time.sort(key=lambda x: x[0])
    
    # 시간표 설정
    time_table = {}  # 각 방의 시간대별 사용가능 시간표
    room_number = 0  # 다음으로 들어갈 방 번호
    
    def time_calculate(time):
        # 시간을 분 단위로 변환
        h, m = time.split(":")
        return 60 * int(h) + int(m)
    
    for t in book_time:
        # 2. 대실 시작 시간, 종료 시간 분리
        start, end = t
        start = time_calculate(start)
        end = min(time_calculate(end) + 10, 24 * 60)  # 자정을 넘기는 경우, 24:00로 설정
        
        # 3. 각 방을 순회하면서 시간대가 겹치지 않는지 체크
        for i in range(len(time_table)):
            # 방이 비어 있으면 그대로 체크인
            if not time_table[i]:
                time_table[i] = (start, end)
                break
            # 시간이 다 되어서 앞 타임 손님이 체크아웃했을 경우 체크인
            elif time_table[i][1] <= start:
                time_table[i] = (start, end)
                break
        # 방을 다 순회했는데도 빈 방이 없을 경우
        else:
            time_table[room_number] = (start, end)
            room_number += 1  # 다음으로 배치될 방 번호

    return len(time_table)