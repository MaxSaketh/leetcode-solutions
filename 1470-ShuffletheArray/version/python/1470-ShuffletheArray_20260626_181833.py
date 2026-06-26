# Last updated: 26/06/2026, 18:18:33
1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        l = int(len(nums)/2)
4        x = nums[:l]
5        y = nums[l:]
6
7        ans = []
8        for i in range(l):
9            ans.append(x[i])
10            ans.append(y[i])
11        return ans