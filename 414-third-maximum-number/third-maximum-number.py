class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        fm = float('-inf')
        sm = float('-inf')
        tm = float('-inf')
        for num in nums:
            if num == fm or num == sm or num == tm:
                continue

            if num > fm:
                tm = sm
                sm = fm
                fm = num
            elif num > sm:
                tm = sm
                sm = num
            elif num > tm:
                tm = num

        return tm if tm != float('-inf') else fm