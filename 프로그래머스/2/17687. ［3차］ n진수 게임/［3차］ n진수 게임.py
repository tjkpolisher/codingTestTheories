def solution(n, t, m, p):
    # n: 진법, t: 미리 구할 숫자의 갯수, m: 게임 참가 인원 수, p: 튜브의 순서
    answer, nums = '', '0'
    mod_table = {10: 'A', 11: 'B', 12: 'C',
                 13: 'D', 14: 'E', 15: 'F'}

    for i in range(1, t * m):
        num = ''
        while i > 0:
            mod = i % n
            if mod >= 10:
                mod = mod_table[mod]
            num += str(mod)
            i //= n
        nums += num[::-1]

    for i in range(p - 1, len(nums), m):
        answer += nums[i]

    return answer[:t]