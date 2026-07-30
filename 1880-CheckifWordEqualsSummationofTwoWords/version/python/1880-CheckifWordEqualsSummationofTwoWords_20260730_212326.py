# Last updated: 30/07/2026, 21:23:26
1class Solution:
2    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
3        num1 = int("".join(str(ord(c) - ord('a')) for c in firstWord))
4        num2 = int("".join(str(ord(c) - ord('a')) for c in secondWord))
5        target = int("".join(str(ord(c) - ord('a')) for c in targetWord))
6
7        return num1 + num2 == target