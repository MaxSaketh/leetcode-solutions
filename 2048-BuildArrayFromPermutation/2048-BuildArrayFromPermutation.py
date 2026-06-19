# Last updated: 19/06/2026, 18:35:18
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in (nums):
            indx = nums.index(i)
            ans.append(nums[nums[indx]])
        return (ans)