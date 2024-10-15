import sys
sys.setrecursionlimit(10**6)

def solution(numbers, target):
    def dfs(index, current_sum):
        # 모든 숫자를 사용했을 경우, 현재 합이 타겟과 같은지 확인
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        # 현재 숫자를 더하는 경우와 빼는 경우에 대하여 재귀 호출
        count_with_plus = dfs(index + 1, current_sum + numbers[index])
        count_with_minus = dfs(index + 1, current_sum - numbers[index])
        
        # 두 경우의 수를 합해서 반환
        return count_with_plus + count_with_minus
    
    return dfs(0, 0)