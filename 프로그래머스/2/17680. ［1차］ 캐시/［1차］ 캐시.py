from collections import deque
def solution(cacheSize, cities):
    # 캐시 크기가 0일 경우 반드시 캐시 미스 발생
    if cacheSize == 0:
        return len(cities) * 5

    answer = 0
    
    cache = deque()  # 캐시를 저장할 큐
    for i, data in enumerate(cities):
        city = data.lower()
        if city not in cache:  # 캐시 미스 상황
            if len(cache) < cacheSize:
                cache.appendleft(city)
            else:
                cache.pop()
                cache.appendleft(city)
            answer += 5
            continue
        else:  # 캐시 히트 상황
            # 해당되는 도시 이름(city)를 큐에서 제거 후 맨 앞으로 이동
            cache.remove(city)
            cache.appendleft(city)
            answer += 1
    
    return answer