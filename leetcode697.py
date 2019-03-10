class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x]=i
            right[x]=i
            if x not in count:
                count[x]=1
            else:
                count[x]+=1
        degree=max(count.values())
        ans=len(nums)
        for x in count:
            if count[x]==degree:
                if right[x]-left[x]+1<ans:
                    ans=right[x]-left[x]+1
        return ans

"""
class Solution:
    def findShortestSubArray(self, nums):

        :type nums: List[int]
        :rtype: int

        dict,thekeys={},[]
        length=len(nums)
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]]=1
            else:
                dict[nums[i]]+=1
        for key,value in dict.items():
            if value==max(dict.values()):
                thekeys.append(key)
        for thekey in thekeys:
            for j in range(len(nums)):
                if nums[j]==thekey:
                    start=j
                    break
            for k in range(len(nums)-1,-1,-1):
                if nums[k]==thekey:
                    end = k
                    break
            temp=end-start+1
            if temp<length:
                length=temp
        return length
"""
solution=Solution()
nums=[1,2,2,3,1,4,2]
print(solution.findShortestSubArray(nums))
