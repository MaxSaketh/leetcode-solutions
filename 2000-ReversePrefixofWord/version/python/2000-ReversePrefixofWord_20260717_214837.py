# Last updated: 17/07/2026, 21:48:37
1class Solution:
2    def reversePrefix(self, word: str, ch: str) -> str:
3        if ch not in word:
4            return word
5        
6        i = word.index(ch)
7
8        return word[i::-1] + word[i+1::]