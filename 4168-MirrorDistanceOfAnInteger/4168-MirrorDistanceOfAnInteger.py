# Last updated: 19/06/2026, 18:35:08
class Solution:
    def mirrorDistance(self, n: int) -> int:
        og = n
        rev = 0
        while n > 0:
            x = n % 10
            rev = rev*(10)+x
            n = n // 10
        ans = og - rev
        return  ans if ans > 0 else ans*(-1)
