class RecentCounter:

    def __init__(self):
        self.nums = []
        self.start = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        count = 0
        self.nums.append(t)
        while len(self.nums) > self.start and self.nums[self.start] < t - 3000:
            self.start += 1
        return len(self.nums) - self.start
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)