class Solution:
    def minHeightShelves(self, books, shelf_width):
        n = len(books)
        dp = [float("inf") for x in range(n + 1)]
        dp[0] = 0
        for i in range(1, n+1):
            j = i-1
            width, max_height = shelf_width, 0
            while j>=0 and width >= books[j][0]:
                width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1
        return dp[n]
                
                
            