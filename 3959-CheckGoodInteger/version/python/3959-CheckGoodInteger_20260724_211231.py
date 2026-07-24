# Last updated: 24/07/2026, 21:12:31
1class Solution:
2    def checkGoodInteger(self, n: int) -> bool:
3        digitSum = 0
4        squareSum = 0
5
6        nums = [int(i) for i in str(n)]
7
8        for i in nums:
9            digitSum += i
10            squareSum += i*i
11        
12        return squareSum - digitSum >= 50