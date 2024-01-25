def solution(dirs):
    # 문제 출처: Summer/Winter Coding(~2018)
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/49994
    x, y = 5, 5
    ans = set() # 겹치는 좌표는 생략해야 하므로 집합 자료형 사용
    for dir in dirs:
        nx, ny = update_location(x, y, dir)
        if not is_valid_move(nx, ny):
            continue
        ans.add((x, y, nx, ny))
        ans.add((nx, ny, x, y)) # A에서 B로 간 경우 B에서 A도 추가해야 함(총 경로의 개수는 방향성이 없음) 
        x, y = nx, ny
    return int(len(ans) / 2)

def is_valid_move(nx, ny):
    # 주어진 좌표평면을 벗어나는지 체크하는 함수
    # 이 함수는 좌표문제에 단골로 등장하니, 잘 참고해봅시다!
    return 0 <= nx < 11 and 0 <= ny < 11

def update_location(x, y, dir):
    # 다음 좌표 결정
    if dir == 'U':
        nx, ny = x, y + 1
    elif dir == 'D':
        nx, ny = x, y - 1
    elif dir == 'L':
        nx, ny = x - 1, y
    elif dir == 'R':
        nx, ny = x + 1, y
    
    return nx, ny

if __name__ == "__main__":
    ex1 = "ULURRDLLU"
    ex2 = "LULLLLLLU"
    for e in [ex1, ex2]:
        print(solution(e))