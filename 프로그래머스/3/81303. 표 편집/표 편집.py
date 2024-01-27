def solution(n, k, cmd):
    original = ['O'] * n # 행의 잔류 혹은 삭제를 저장하는 리스트
    k += 1 # 표의 위아래로 가상 인덱스를 만들기 때문에 k에 1을 더해줌
    deleted = [] # 삭제된 행을 저장해놓을 스택
    
    up = [i - 1 for i in range(n + 2)] # 각 행의 위 행 인덱스
    down = [i + 1 for i in range(n + 1)] # 각 행의 아래 행 인덱스
    
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