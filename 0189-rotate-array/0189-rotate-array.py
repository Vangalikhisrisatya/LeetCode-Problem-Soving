class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        ans=[]
        k=k%n
        for i in range(n-k,n):
            ans.append(nums[i])
        for i in range(n-k):
            ans.append(nums[i])
        for i in range(len(ans)):
            nums[i]=ans[i]
        return nums
        
        