class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        nums = [0 for i in range(60)]
        count, n = 0, len(time)
        for i in range(n):
            target = (60 - time[i] % 60) % 60
            count += nums[target]
            nums[time[i] % 60] += 1
        return count
s1=Solution()
str=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s1.gameOfLife(str)
print(str)
