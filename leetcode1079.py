class Solution:
    def numTilePossibilities(self, tiles):
        self.res = 0
        self.seen = set()
        self.dfs(tiles, "")
        return self.res 
    
    def dfs(self, tiles, path):
        if not tiles:
            if path!="" and path not in self.seen:
                self.seen.add(path)
                self.res += 1
                return
        for i in range(len(tiles)):
            self.dfs(tiles[:i] + tiles[i + 1:], path)
            self.dfs(tiles[:i] + tiles[i + 1:], path + tiles[i])

TLE

class Solution:
    def numTilePossibilities(self, tiles):
        self.res = 0
        self.seen = set()
        self.dfs(tiles, "")
        return self.res
    
    def dfs(self, tiles, path):
        if path!="" and path not in self.seen:
            self.seen.add(path)
            self.res += 1
        for i in range(len(tiles)):
            self.dfs(tiles[:i] + tiles[i + 1:], path + tiles[i])
			
稍加修改之后可以通过