class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = list(s.split())[-1]
        return len(last_word)