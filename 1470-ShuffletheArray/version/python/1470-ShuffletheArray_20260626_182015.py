# Last updated: 26/06/2026, 18:20:15
# used `n` directly from input rather than calculating again
1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        x = nums[:n]
4        y = nums[n:]
5
6        ans = []
7        for i in range(n):
8            ans.append(x[i])
9            ans.append(y[i])
10        return ans