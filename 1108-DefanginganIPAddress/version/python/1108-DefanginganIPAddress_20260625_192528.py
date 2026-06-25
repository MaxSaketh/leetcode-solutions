# Last updated: 25/06/2026, 19:25:28
# replace func()
1class Solution:
2    def defangIPaddr(self, address: str) -> str:
3        return address.replace('.', '[.]')
4