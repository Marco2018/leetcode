class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n=len(bits)
        count=0
        for i in range(n-2,-1,-1):
            if bits[i]==1:
                count+=1
            else:
                break
        if count%2==0:
            return True
        else:
            return False
solution=Solution()
list=[1,0,0]
print(solution.isOneBitCharacter(list))

#判断最后一个0到前一个0之间有多少个1
