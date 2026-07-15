class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=0
        sumEven=0
        for i in range(1,2*n+1):
            if i%2==0:
                sumEven+=1
            else:
                sumOdd+=1
        while sumEven!=0:
            sumOdd,sumEven=sumEven,sumOdd%sumEven
        return sumOdd


        