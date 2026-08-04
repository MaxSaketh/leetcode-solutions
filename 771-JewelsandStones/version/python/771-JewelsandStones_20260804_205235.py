# Last updated: 04/08/2026, 20:52:35
1class Solution:
2    def numJewelsInStones(self, jewels: str, stones: str) -> int:
3        count = 0 
4        
5        for i in jewels:
6            count += stones.count(i)
7
8        return count