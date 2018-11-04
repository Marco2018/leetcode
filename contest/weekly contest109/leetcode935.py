class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==1:
            return 10
        nums=[1 for i in range(10)]
        temp=[1 for i in range(10)]
        times=1
        while times<N:
            nums[0]=temp[4]+temp[6]
            nums[1]=temp[6]+temp[8]
            nums[2]=temp[9]+temp[7]
            nums[3]=temp[4]+temp[8]
            nums[4]=temp[3]+temp[9]+temp[0]
            nums[5]=0
            nums[6]=temp[0]+temp[1]+temp[7]
            nums[7]=temp[2]+temp[6]
            nums[8]=temp[1]+temp[3]
            nums[9]=temp[2]+temp[4]
            temp=nums.copy()
            times+=1
        ans=sum(nums)%(10**9+7)
        return ans