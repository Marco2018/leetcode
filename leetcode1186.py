class Solution:
    def maximumSum(self, arr):
        n, temp = len(arr), 0
        left, right = [-float("inf") for i in range(n)], [-float("inf") for i in range(n)]
        for i in range(n):
            temp += arr[i]
            right[i] = max(arr[i], temp)
            if temp < 0:
                temp = 0
        temp = 0
        for i in range(n-1, -1, -1):
            temp += arr[i]
            left[i] = max(arr[i], temp)
            if temp < 0:
                temp = 0
        res = max(max(left), max(right))
        for i in range(1, n-1, 1):
            res = max(res, right[i-1] + left[i+1])
        return res