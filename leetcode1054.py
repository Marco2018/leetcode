class Solution:
    def rearrangeBarcodes(self, barcodes):
        count = collections.Counter(barcodes)
        res = []
        q = []
        for item, val in count.items():
            q.append([-val, item])
        heapq.heapify(q)
        while q:
            val, item = heapq.heappop(q)
            if len(res) == 0 or res[-1]!=item:
                res.append(item)
                if val != -1:
                    heapq.heappush(q, [val + 1, item])
            else:
                val2, item2 = heapq.heappop(q)
                heapq.heappush(q, [val, item])
                res.append(item2)
                if val2 != -1:
                    heapq.heappush(q, [val2 + 1, item2])
        return res