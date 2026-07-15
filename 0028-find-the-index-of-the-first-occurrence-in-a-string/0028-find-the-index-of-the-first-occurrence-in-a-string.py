class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j=len(needle)
       
        for i in range(len(haystack)):
            if haystack[i:j]!=needle:
                j+=1
                
            else:
                return i
        return -1

        
