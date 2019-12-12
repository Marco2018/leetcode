class Solution:

    def trapRainWater(self, grid):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        heap = []
        visit = set()
        # init , put surrounding into heap
        for i in [0, m - 1]:
            for j in range(n):
                heap.append((grid[i][j], i, j))
                visit.add((i, j))

        for j in [0, n - 1]:
            for i in range(1, m-1):
                heap.append((grid[i][j], i, j))
                visit.add((i, j))

        heapq.heapify(heap)

        dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = 0
        mx = float('-inf')

        while heap:

            h, x, y = heapq.heappop(heap)
            mx = max(h, mx)

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                if (nx, ny) in visit:
                    continue

                if mx > grid[nx][ny]:
                    ans += mx - grid[nx][ny]

                itm = (grid[nx][ny], nx, ny)
                heapq.heappush(heap, itm)
                visit.add((nx, ny))

        return ans