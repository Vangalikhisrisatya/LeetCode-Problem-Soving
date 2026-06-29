class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        j=1
        n=len(nums)
        for i in range(n):
            if nums[i]>=target:
                return i
        return n
        