# Last updated: 29/07/2026, 19:50:13
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        a = ""
4        
5        for i in s:
6            if i.isalnum():
7                a += i.lower()
8
9        return a == a[::-1]
10        