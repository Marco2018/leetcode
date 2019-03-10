class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor<0:
            isminus=1
            divisor=-divisor
        else:
            isminus=0
        if dividend<0:
            isminus2=1
            dividend=-dividend
        else:
            isminus2=0
        count=0
        while dividend>=divisor:
            temp=divisor
            k=1
            while dividend>=temp:
                dividend -= temp
                count=count+k
                k=k*2
                temp=temp*2
        if isminus==1:
            count=-count
        if isminus2==1:
            count=-count
        if count<=pow(2,31)-1:
            return count
        else:
            return pow(2,31)-1



object1=Solution()
dividend = 10
divisor = 3
print(Solution.divide(object1,-7,-3))

#为了加速运算，可以依次将被除数减去1，2，4，8，..倍的除数。
