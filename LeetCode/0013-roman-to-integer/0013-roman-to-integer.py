class Solution:
    def romanToInt(self, s: str) -> int:
        sv_table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i, c in enumerate(s):
            n = sv_table[c]
            if i < len(s) - 1 and n < sv_table[s[i + 1]]:
                ans -= n
            else:
                ans += n
        return ans

        