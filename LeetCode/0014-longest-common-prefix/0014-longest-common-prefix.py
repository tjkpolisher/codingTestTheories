class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        answer = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                answer += strs[0][i]
            else:
                break
        return answer
