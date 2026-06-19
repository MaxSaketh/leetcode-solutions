# Last updated: 19/06/2026, 18:35:09
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        result = 0
        for i in str(n):
            result += int(i)
        return result

