def solution(arr1, arr2):
    # m * n 행렬 arr1과 n * p 행렬 arr2를 곱한 결과 행렬의 크기 m * p
    m = len(arr1)  # arr1의 행의 개수
    p = len(arr2[0])  # arr2의 열의 개수
    n = len(arr2)  # arr2의 행의 개수 (= arr1의 열의 개수)
    
    answer = [[0] * p for _ in range(m)]  # m행 n열의 행렬
    
    for i in range(m):
        for j in range(p): 
            for k in range(n): 
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer