def possible(answer):
    # 설치가 가능한지 판단하는 함수
    for x, y, stuff in answer:
        if not stuff:  # 기둥일 경우
            if not y or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                # 각각 바닥 위, 보의 한쪽 끝 부분 위, 다른 기둥 위에 있는 경우를 뜻함
                # 이 경우는 정상이므로 continue
                continue
            return False
        elif stuff == 1:  # 보일 경우
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                # 각각 한쪽 끝부분이 기둥 위, 양쪽 끝 부분이 다른 보와 동시에 연결을 뜻함
                # 이 경우는 정상이므로 continue
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if not operate:  # 삭제
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:  # 설치
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    
    return sorted(answer)