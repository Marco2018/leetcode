class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            a=nums.pop()
            nums.insert(0,a)
        return nums

object1=Solution()
numbers = [1,2,3,4,5,6,7]
target = 2
print(Solution.rotate(object1,numbers,target))

'''def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(numbers)):
            if target-numbers[i] in numbers[i+1:]:
               return [i+1,numbers[i+1:].index(target-numbers[i])+1+i+1]
'''