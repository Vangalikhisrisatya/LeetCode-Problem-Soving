from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        si=Counter(s)
        ti=Counter(t)
        if si==ti:
            return True
        else:
            return False
        