class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n=len(nums)
        if n==0:
            return []
        elif n==1:
            return [str(nums[0])]
        start=0
        i=1
        res=[]
        while True:
            if i==n-1:
                if nums[i] != nums[i - 1] + 1:
                    if start!=i-1:
                        res.append(str(nums[start]) + "->" + str(nums[i-1]))
                    else:
                        res.append(str(nums[start]))
                    res.append(str(nums[i]))
                else:
                    res.append(str(nums[start]) + "->" + str(nums[i]))
                break
            if nums[i]!=nums[i-1]+1:
                if start!=i-1:
                    res.append(str(nums[start])+"->"+str(nums[i-1]))
                else:
                    res.append(str(nums[i-1]))
                start=i
            i+=1
        return res
s1=Solution()
nums=[1,3]
print(s1.summaryRanges(nums))