# Last updated: 28/07/2026, 19:21:27
1class Solution:
2    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
3        word1 = "".join(word1)
4        word2 = "".join(word2)
5
6        # for i in word1:
7        #     aword1 += i
8        # for i in word2:
9        #     aword2 += i
10        
11        return word1 == word2