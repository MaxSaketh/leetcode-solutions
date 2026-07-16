# Last updated: 16/07/2026, 18:28:49
1class Solution:
2    def convertDateToBinary(self, date: str) -> str:
3        split = [int(x) for x in date.split("-")]
4
5        return f"{split[0]:b}-{split[1]:b}-{split[2]:b}"