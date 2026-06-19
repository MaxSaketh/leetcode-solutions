# Last updated: 19/06/2026, 18:35:14
class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1):
            ans += abs(ord(s[i])-ord(s[i+1]))
        return ans