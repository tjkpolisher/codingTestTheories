from collections import deque
def solution(maps):
    # X는 바다를, 숫자는 무인도를 나타냄.
    answer = []
    # 1. maps의 문자열 원소를 하나하나 문자로 쪼개고 리스트로 변환
    len1 = len(maps)
    len2 = len(maps[0])
    for i in range(len1):
        maps[i] = list(maps[i])
    
    # 2. BFS를 실시하면서 전체 섬의 수를 더함
    def bfs(i, j, score):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        score = int(maps[i][j])
        maps[i][j] = 'X'  # 시작점도 큐에 넣는 즉시 방문 처리
        
        q = deque()
        q.append((i, j))
        
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < len1 and 0 <= ny < len2:
                    if maps[nx][ny] != 'X':
                        score += int(maps[nx][ny])
                        maps[nx][ny] = 'X'  # 식량 수집 후, 해당 칸은 방문 처리
                        q.append((nx, ny))
        return score
    
    for i in range(len1):
        for j in range(len2):
            if maps[i][j] != 'X':
                tmp = 0
                score = bfs(i, j, tmp)
                answer.append(score)
    
    # 3. 리스트가 비었으면(지낼 수 있는 무인도가 없으면) -1 리턴
    if not answer:
        return [-1]
    # 4. 그 외의 경우, 리스트를 오름차순 정렬 후 리턴
    return sorted(answer)