def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    # prev: 10초 전으로 이동. pos가 10 미만인 경우 영상 처음(0분 0초)으로 이동
    # next: 10초 후로 이동. 남은 시간이 10초 미만인 경우 마지막 위치(video_len)로 이동.
    # 단, op_start <= pos <= op_end인 경우 자동으로 오프닝이 끝나는 위치로 이동.
    
    def time_split(time):
        time_m, time_s = time.split(":")
        time_len = int(time_m) * 60 + int(time_s)
        return time_len
    
    video_len = time_split(video_len)
    pos = time_split(pos)
    op_start = time_split(op_start)
    op_end = time_split(op_end)
    
    # 작업 수행 전, 오프닝 구간은 자동으로 끝으로 이동.
    if op_start <= pos <= op_end:
        pos = op_end
    
    for command in commands:
        if command == 'next':
            pos += 10
            if pos > video_len:
                pos = video_len
        elif command == 'prev':
            pos -= 10
            if pos < 0:
                pos = 0
        if op_start <= pos <= op_end:
            pos = op_end
    
    pos_m, pos_s = divmod(pos, 60)
    return f"{pos_m:02d}:{pos_s:02d}"