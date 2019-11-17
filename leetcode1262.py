import heapq
class Solution:
    def maxSumDivThree(self, nums):
        ones = []
        twos = []
        total = sum(nums)
        total_yu = total % 3
        for num in nums:
            yu = num % 3
            if yu == 1:
                heapq.heappush(ones, num)
            elif yu == 2:
                heapq.heappush(twos, num)

        if total_yu == 0:
            return total
        elif total_yu == 1:
            remove = float("inf")
            if len(ones) > 0:
                remove = min(remove, ones[0])
            if len(twos) > 1:
                remove = min(remove, sum(heapq.nsmallest(2, twos)))
            return total-remove
        else:
            remove = float("inf")
            if len(twos) > 0:
                remove = min(remove, twos[0])
            if len(ones) > 1:
                remove = min(remove, sum(heapq.nsmallest(2, ones)))
            return total-remove