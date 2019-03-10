class Solution:
    def findMinHeightTrees(self,n, edges):
        if n <= 1:
            return [0]
        degrees = [0] * n
        graph = {x: [] for x in range(n)}
        for p in edges:
            degrees[p[1]] += 1
            degrees[p[0]] += 1
            graph[p[1]].append(p[0])
            graph[p[0]].append(p[1])
        queue = [x for x in range(0, n) if degrees[x] == 1]
        ret = []
        #先找叶子节点 然后假装将叶子节点去掉找上一层的节点
        while queue:
            temp = []
            ret = queue[:]
            for x in queue:
                for n in graph[x]:
                    degrees[n] -= 1
                    if degrees[n] == 1:
                        temp.append(n)
            queue = temp

        return ret
s1=Solution()
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(s1.findMinHeightTrees(n,edges))