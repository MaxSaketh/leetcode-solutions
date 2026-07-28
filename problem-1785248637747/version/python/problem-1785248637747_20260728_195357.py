# Last updated: 28/07/2026, 19:53:57
1class Solution:
2    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
3        word1 = "".join(word1)
4        word2 = "".join(word2)        
5        return word1 == word2