def solution(array):
    # set() 함수는 해시 알고리즘으로 데이터를 저장합니다.
    # 해시 알고리즘 자체의 시간 복잡도는 O(1)
    # 다만, 이 경우는 중복값 제거를 위해 리스트를 순회하므로 시간 복잡도는 O(N)
    
    new = list(set(array))
    new.sort(reverse=True)
    
    return new

if __name__ == '__main__':
    ex1 = [4, 2, 2, 1, 3, 4]
    ex2 = [2, 1, 1, 3, 2, 5, 4]
    for e in [ex1, ex2]:
        print(solution(e))