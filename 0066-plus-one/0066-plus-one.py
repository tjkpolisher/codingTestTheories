class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        num = int(''.join(digits))
        num += 1
        digits = list(str(num))
        return [int(i) for i in digits]