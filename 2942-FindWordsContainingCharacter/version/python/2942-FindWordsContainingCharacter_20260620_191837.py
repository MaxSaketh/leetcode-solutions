# Last updated: 20/06/2026, 19:18:37
1class Solution:
2    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
3        indices = []
4        for i in range(len(words)):
5            if x in words[i]:
6                indices.append(i)
7        return indices
8