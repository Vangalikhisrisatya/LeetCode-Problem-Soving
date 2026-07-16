class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if s==goal:
            return True
        n=len(s)
        for i in range(1,n):
            ans=s[i:]+s[:i]
            if ans==goal:
                return True
        return False
        