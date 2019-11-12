class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def subarray(k):
            ans, i = 0, 0
            n = len(nums)
            for j in range(n):
                k -= nums[j]%2
                while (k < 0):
                    k += nums[i]%2
                    i += 1
                ans += j - i + 1
            return ans
        return subarray(k) - subarray(k-1)
        