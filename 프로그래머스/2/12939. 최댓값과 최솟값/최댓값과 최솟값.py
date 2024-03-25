def solution(s):
    s_list = list(map(int, s.split()))
    ans = []
    ans.append(str(min(s_list)))
    ans.append(str(max(s_list)))
    answer = ' '.join(ans)
    return answer