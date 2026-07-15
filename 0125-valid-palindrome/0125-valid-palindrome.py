class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if i.isalnum():
                a=a+i
        i=0
        j=len(a)-1
        a=a.lower()
        while j>=i:
            if a[i]!=a[j]:
                return False
            i+=1
            j-=1
        return True
               
