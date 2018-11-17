class Solution:
    def search(self, nums, target):
        if not nums:
            return False
        left,right=0,len(nums)-1
        while left<=right:
            mid=int((left+right)/2)
            if nums[mid]==target:
                return True
            if nums[mid]>nums[left]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[mid]<nums[left]:
                if nums[right]>=target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                return self.search(nums[left:mid],target) or self.search(nums[mid+1:right+1],target)
        return False
s1=Solution()
nums =[1,3,1,1,1]
target = 3
print(s1.search(nums,target))