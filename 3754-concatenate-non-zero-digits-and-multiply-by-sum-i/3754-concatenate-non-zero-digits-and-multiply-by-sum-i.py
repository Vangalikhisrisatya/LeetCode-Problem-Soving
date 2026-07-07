class Solution:
    def sumAndMultiply(self, n: int) -> int:
        a=str(n)
        sum=0
        res=""
        for i in range(len(a)):
            if a[i]!="0":
                res=res+a[i]
        if res=="":
            return 0
        for i in range(len(res)):
            sum=sum+int(res[i])

        return int(res)*sum
        