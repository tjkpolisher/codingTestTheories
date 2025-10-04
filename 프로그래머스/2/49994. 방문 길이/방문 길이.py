def solution(dirs):
    answer = 0
    
    orig = [0, 0]  # 최초 시작 위치
    routes = set()  # 지나간 길을 기록할 집합
    dir_dict = {'U': [0, 1], 'D': [0, -1],
                'R': [1, 0], 'L': [-1, 0]}
    
    for dir in dirs:
        diff = dir_dict[dir]  # 이동 방향에 따른 좌표 이동
        moved = [orig[0] + diff[0], orig[1] + diff[1]]
        
        # 이동 후 보드 위를 벗어날 경우 정지
        if moved[0] < -5 or moved[0] > 5 or moved[1] < -5 or moved[1] > 5:
            continue
        element = [tuple(orig), tuple(moved)]
        element.sort(key=lambda x: (x[0], x[1]))  # 중복 방지를 위해 정렬
        if tuple(element) not in routes:
            answer += 1
            routes.add(tuple(element))
        orig = moved  # orig 변수를 새 위치(moved)로 갱신
        
    return answer