class Solution:
    def isPalindrome(self, x: int) -> bool:
        j=len(str(x))-1
        i=0
        while i<=j:
            if str(x)[i]==str(x)[j]:
                i+=1
                j-=1
            else:
                return False
        return True

        