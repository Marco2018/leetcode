class Solution:
    def nextPermutation(self, nums):
        n=len(nums)
        if n<=1:
            return
        i=n-2
        while i>=0:
            if nums[i]<nums[i+1]:
                break
            i-=1
        if i<0:
            nums.sort()
            return
        min_number=nums[i+1]-nums[i]
        min_index=i+1
        for j in range(i+1,n,1):
            if nums[j]>nums[i] and nums[j]-nums[i]<min_number:
                min_number=nums[j]-nums[i]
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]
        temp=nums[i+1:]
        temp.sort()
        nums[i+1:]=temp
        return
s1=Solution()
nums=[1,3,2]
print(s1.nextPermutation(nums))