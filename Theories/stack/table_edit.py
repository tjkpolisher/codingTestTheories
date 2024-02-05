def solution(n, k, cmd):
    # 문제 출처: 2021 카카오 채택연계형 인턴십
    # 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/81303
    # U X: 현재 행에서 X칸 위에 있는 행 선택
    # D X: 현재 행에서 X칸 아래에 있는 행 선택
    # C: 현재 행을 삭제한 후, 바로 아래 행을 선택(단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행 선택)
    # Z: 가장 최근에 삭제한 행을 원래대로 복구(단, 현재 선택한 행은 바뀌지 않음)
    original = ['O'] * n  # 행의 잔류 혹은 삭제를 저장하는 리스트
    k += 1  # 표의 위아래로 가상 인덱스를 만들기 때문에 k에 1을 더해줌
    deleted = []  # 삭제된 행을 저장해놓을 스택
    
    up = [i - 1 for i in range(n + 2)]  # 각 행의 위 행 인덱스
    down = [i + 1 for i in range(n + 1)]  # 각 행의 아래 행 인덱스
    
    for c in cmd:
        if c.startswith("C"):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
        
        elif c.startswith("Z"):
            popped = deleted.pop()
            down[up[popped]] = popped
            up[down[popped]] = popped
        
        else:
            action, num = c.split()
            if action == 'U':
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]
            
    for i in deleted:
        original[i - 1] = 'X'
            
    return ''.join(original)

if __name__ == "__main__":
    ex1 = [8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]]
    ex2 = [8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]]
    for e in [ex1, ex2]:
        print(solution(e[0], e[1], e[2]))