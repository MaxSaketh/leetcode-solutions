# Last updated: 30/07/2026, 20:43:43
1class Solution:
2    def countSeniors(self, details: List[str]) -> int:
3        count = 0
4        for i in details:
5            age = int(i[11:13])
6            if age > 60:
7                count += 1
8        return count
9