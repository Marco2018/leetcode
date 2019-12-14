from collections import defaultdict
class Solution:
    def get_depth(self, graph, nu):
        if len(graph[nu]) != 0:
            if self.isvisited[nu] == 1:
                return self.depth[nu]
            else:
                self.depth[nu] = 1 + max([self.get_depth(graph, node) for node in graph[nu]])
                self.isvisited[nu] = 1
                return self.depth[nu]
        else:
            return 1

    def dfs(self, graph, start, isvisited, stack):
        isvisited[start] = 0
        for node in graph[start]:
            if isvisited[node] == -1:
                self.dfs(graph, node, isvisited, stack)
            if isvisited[node] == 0:
                self.flag = False
                return
        stack.insert(0, start)
        isvisited[start] = 1
        return

    def minimumSemesters(self, N, relations):
        if N <= 1: return N
        visited = [-1 for i in range(N+1)]
        graph = defaultdict(set)
        for s, e in relations:
            graph[s].add(e)
        stack = []
        self.flag = True
        for i in range(1, N+1):
            if visited[i] == -1:
                self.dfs(graph, i, visited, stack)
        if not self.flag:
            return -1
        self.isvisited = [0 for i in range(N + 1)]
        self.depth = [-1 for i in range(N + 1)]
        res = 1
        for i in range(1, N + 1):
            if self.isvisited[i] == 0:
                self.depth[i] = self.get_depth(graph, i)
                self.isvisited[i] = 1
                res = max(res, self.depth[i])
        return res