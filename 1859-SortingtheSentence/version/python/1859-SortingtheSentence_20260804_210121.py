# Last updated: 04/08/2026, 21:01:21
1class Solution:
2    def sortSentence(self, s: str) -> str:
3        words = s.split()
4        words.sort(key=lambda x: x[-1])
5        return " ".join(word[:-1] for word in words)