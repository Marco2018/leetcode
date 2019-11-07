class Solution:    def findMin(self, nums: List[int]) -> int:        left, right, n = 0, len(nums)-1, len(nums)        while left < right:            mid = int((left + right) / 2)            if nums[mid] > nums[right]:                left = mid + 1            elif nums[mid] < nums[right]:                right = mid            else:                right -= 1        return nums[left]   