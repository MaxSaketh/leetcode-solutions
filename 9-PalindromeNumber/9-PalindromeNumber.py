# Last updated: 19/06/2026, 19:06:52
class Solution:
    def isPalindrome(self, x: int) -> bool:
        og = x
        pal = 0
        while x > 0:
            l = x % 10
            pal = pal*10 + l
            x = x // 10
        return (True if og == pal else False)
