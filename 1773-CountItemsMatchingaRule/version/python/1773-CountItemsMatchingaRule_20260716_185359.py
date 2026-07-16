# Last updated: 16/07/2026, 18:53:59
1class Solution:
2    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
3        count = 0
4        for i in items:
5            if ruleKey =="type":
6                count += i[0] == ruleValue
7            elif ruleKey == "color":
8                count += i[1] == ruleValue
9            else:
10                count += i[2] == ruleValue
11        
12        return count