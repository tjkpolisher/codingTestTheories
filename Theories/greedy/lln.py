def lln():
    import sys
    n, m, k = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    big1 = max(nums)
    big2 = nums[n-2]
    
    count = int(m / (k + 1)) * k
    count += m % (k + 1)
    
    result = 0
    result += count * big1
    result += (m - count) * big2
    print(result)

if __name__=="__main__":
    lln()