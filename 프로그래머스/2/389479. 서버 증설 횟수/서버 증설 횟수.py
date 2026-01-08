def solution(players, m, k):
    n = len(players)
    active_servers = [0] * n
    answer = 0
    
    for i, n in enumerate(players):
        if i - k >= 0 and active_servers[i - k] > 0:
            active_servers[i - k] = 0
        
        if n // m > 0 and n // m > sum(active_servers):
            tmp = n // m - sum(active_servers)
            active_servers[i] = tmp
            answer += tmp
    
    return answer