class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        length1,length2=len(nums1),len(nums2)
        if length1==0 or length2==0:
            return []
        all_nums=[]
        for i in range(length1):
            for j in range(length2):
                all_nums.append([nums1[i],nums2[j],nums1[i]+nums2[j]])
        all_nums.sort(key=lambda x:(x[2]))
        number=min(k,len(all_nums))
        return [[all_nums[i][0],all_nums[i][1]] for i in range(number)]