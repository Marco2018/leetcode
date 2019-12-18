class Solution:
    def assignBikes(self, workers, bikes):
        nums = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                d = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                nums.append([d, i, j])
        nums.sort()
        res = [0 for i in range(len(workers))]
        seen_workers, seen_bikes = set(), set()
        for d, i, j in nums:
            if i not in seen_workers and j not in seen_bikes:
                seen_workers.add(i)
                seen_bikes.add(j)
                res[i] = j
        return res