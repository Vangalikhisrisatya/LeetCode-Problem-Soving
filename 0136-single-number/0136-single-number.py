from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums1=Counter(nums)
        for i in nums1:
            if nums1[i]==1:
                return i

        