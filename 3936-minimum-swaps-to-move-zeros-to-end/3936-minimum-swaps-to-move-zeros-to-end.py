class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        count=0
        i=0
        j=len(nums)-1
        while(i<=j):
            if nums[j]==0:
                j-=1
            elif nums[i]!=0:
                i+=1
            else:
                count+=1
                i+=1
                j-=1
        return count