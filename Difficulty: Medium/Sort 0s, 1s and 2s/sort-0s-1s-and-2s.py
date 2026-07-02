class Solution:
    def sort012(self, arr):
        # code here
        n=len(arr)
        start = 0
        end = n-1
        temp = 0
        while end>=temp:
            if arr[temp]==0:
                arr[temp],arr[start]=arr[start],arr[temp]
                start+=1
                temp+=1
            elif arr[temp]==2:
                arr[temp],arr[end]=arr[end],arr[temp]
                end-=1
            else:
                temp+=1
        return arr
        
            