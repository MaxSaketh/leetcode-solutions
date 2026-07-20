# Last updated: 20/07/2026, 21:02:56
1class Solution:
2    def mostWordsFound(self, sentences: List[str]) -> int:
3        x = [len(i.split(" ")) for i in sentences]
4        return max(x)