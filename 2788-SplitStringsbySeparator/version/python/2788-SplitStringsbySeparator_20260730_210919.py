# Last updated: 30/07/2026, 21:09:19
1class Solution:
2    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
3        x = []
4        for i in words:
5            x.extend(i.split(separator))
6        return [i for i in x if len(i) >= 1]