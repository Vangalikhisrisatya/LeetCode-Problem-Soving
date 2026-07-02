class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        se=list(s)
        te=list(t)
        se.sort()
        te.sort()
        n=len(se)
        i=0
        for i in range(n):
            if se[i]!=te[i]:
                return te[i]
        return te[-1]    
