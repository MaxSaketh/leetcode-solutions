# Last updated: 19/06/2026, 19:08:32
1# String method
2class Solution:
3    def isPalindrome(self, x: int) -> bool:
4        return str(x)==str(x)[::-1]