class Solution(object):    def checkPossibility(self, nums):        """        :type nums: List[int]        :rtype: bool        """        n=len(nums)        if n<=2:            return True        left,right=[0 for i in range(n)],[0 for i in range(n)]        left[0]=nums[0]        for i in range(1,n):            left[i]=max(left[i-1],nums[i])        right[n-1]=nums[n-1]        for j in range(n-2,-1,-1):            right[j]=min(right[j+1],nums[j])        #print(left,right)        times_left,times_right=0,0        for k in range(n):            if nums[k]<left[k]:                times_left+=1            if nums[n-1-k]>right[n-1-k]:                times_right+=1        if times_left>1 and times_right>1:            return False        return Trues = Solution()nums = [3,4,2,3]print(s.checkPossibility(nums))