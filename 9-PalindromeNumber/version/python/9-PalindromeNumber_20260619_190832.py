# Last updated: 19/06/2026, 19:08:32
# String method
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
