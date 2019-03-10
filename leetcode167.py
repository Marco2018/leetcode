class Solution:
    def twoSum(self, numbers, target):
        dic = {}
        for i in range(len(numbers)):
            if numbers[i] in dic:
                return [dic[numbers[i]] + 1, i + 1]
            else:
                dic[target - numbers[i]] = i
object1=Solution()
numbers = [0,0,11,15]
target = 0
print(Solution.twoSum(object1,numbers,target))

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