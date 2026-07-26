# Last updated: 26/07/2026, 20:14:48
1class Solution:
2    def restoreString(self, s: str, indices: List[int]) -> str:
3        res = [''] * len(s)
4        for i in range(len(s)):
5            res[indices[i]] = s[i]
6        return "".join(res)