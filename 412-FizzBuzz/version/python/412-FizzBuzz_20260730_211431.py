# Last updated: 30/07/2026, 21:14:31
1class Solution:
2    def fizzBuzz(self, n: int) -> List[str]:
3        x = []
4        for i in range(1,n+1):
5            if i % 3 == 0 and i % 5 == 0:
6                x.append("FizzBuzz")
7            elif i % 3 == 0:
8                x.append("Fizz")
9            elif i % 5 == 0:
10                x.append("Buzz")
11            else:
12                x.append(str(i))
13        return x