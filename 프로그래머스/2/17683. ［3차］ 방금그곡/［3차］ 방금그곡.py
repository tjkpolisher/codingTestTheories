def solution(m, musicinfos):
    """
    m: 네오가 기억한 멜로디(str)
    musicinfos: 방송된 곡의 정보를 담은 배열(list)
    """
    answer = "(None)"
    candidate = []
    
    for i, info in enumerate(musicinfos):
        # 정보 분할: 시작 시각, 끝난 시각, 음악 제목, 악보 정보
        start_time, end_time, title, melody = info.split(',')
        a, b = map(int, start_time.split(':'))
        c, d = map(int, end_time.split(':'))
        playtime = c * 60 + d - a * 60 - b  # 재생 시간
        
        # 멜로디 일치 여부 확인
        melody_list = list(melody)
        for idx, mel in enumerate(melody_list):
            if mel == '#':
                melody_list[idx - 1] += '#'
        melody_list = [mel for mel in melody_list if mel != '#']
        
        length = len(melody_list)
        real = ''
        for i in range(playtime):
            tmp = i % length
            real += melody_list[tmp]
        
        if m in real:
            if real.count(m) > real.count(m + '#'):  # #(샵)이 포함된 문자열 필터링 조건
                candidate.append([playtime, title, i])
    
    if candidate:
        candidate.sort(key=lambda x:(-x[0], x[2]))  # 재생 시간 내림차순, 먼저 입력된 제목 순서 오름차순 정렬
        return candidate[0][1]
    
    # 후보가 없을 경우 그대로 "(None)" 반환
    return answer