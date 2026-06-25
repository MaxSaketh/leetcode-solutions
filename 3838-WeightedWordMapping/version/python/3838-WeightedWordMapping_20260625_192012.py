# Last updated: 25/06/2026, 19:20:12
1class Solution:
2    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
3        alpha = list("abcdefghijklmnopqrstuvwxyz")
4        rev = sorted(alpha, reverse=True)
5        ans = ""
6        for i in words:
7            sum = 0
8            for j in i:
9                sum += weights[alpha.index(j)]
10            ans += rev[(sum % 26)]
11        return ans