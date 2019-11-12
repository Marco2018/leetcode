class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        def subarray(K):
            nums = [0 for i in range(len(A) + 1)]
            i = 0
            ans = 0
            for j in range(len(A)):
                if nums[A[j]] == 0: #如果A[j]是第一次出现，则K-1
                    K -= 1
                nums[A[j]] += 1
                while (K < 0):  #如果在i,j 之间的数字已经超过K个了 则开始移动i
                    if nums[A[i]] == 1: #如果==1 则当i右移时A[i]这个数字将会从substring中移除
                        K += 1
                    nums[A[i]] -= 1
                    i += 1
                ans += j - i + 1 # 一共有j-i+1 substring
            return ans
        return subarray(K) - subarray(K-1)