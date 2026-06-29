class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_cnt=0
        for i in range(len(nums)):
            if nums[i]==1:
                count=count+1
                max_cnt=max(count,max_cnt)
            else:
                count=0
                
        return max_cnt
        