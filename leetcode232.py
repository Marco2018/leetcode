class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.nums.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        res = self.nums[0]
        self.nums = self.nums[1:]
        return res

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.nums[0]
s1=Solution()
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(s1.findMinHeightTrees(n,edges))