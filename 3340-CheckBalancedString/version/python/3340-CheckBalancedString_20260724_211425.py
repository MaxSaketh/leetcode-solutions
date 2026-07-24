# Last updated: 24/07/2026, 21:14:25
1class Solution:
2    def isBalanced(self, num: str) -> bool:
3        e = sum([int(i) for i in num[0::2]])
4        o = sum([int(i) for i in num[1::2]])
5
6        return e == o