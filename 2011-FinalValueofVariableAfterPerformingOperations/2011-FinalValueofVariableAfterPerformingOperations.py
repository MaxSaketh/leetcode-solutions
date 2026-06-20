# Last updated: 20/06/2026, 19:13:04
1class Solution:
2    def finalValueAfterOperations(self, operations: List[str]) -> int:
3        init = 0
4
5        for i in operations:
6            if i in ["++X","X++"]:
7                init += 1
8            else: 
9                init -= 1
10        return init