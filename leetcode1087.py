class Solution:
    def dfs(self, chars, path):
        if not chars:
            self.res.append(path)
            return
        if len(chars[0]) == 1:
            self.dfs(chars[1:], path + chars[0][0])
        else:
            for i in range(len(chars[0])):
                self.dfs(chars[1:], path + chars[0][i])
        return

    def expand(self, S):
        chars = []
        n, i = len(S), 0
        temp = []
        while i<n:
            if S[i] == "{":
                temp = []
                i += 1
                while S[i]!="}":
                    if S[i] != ",":
                        temp.append(S[i])
                    i += 1
                if S[i] == "}":
                    temp.sort()
                    chars.append(temp)
                    i += 1
            else:
                chars.append([S[i]])
                i += 1
        self.res = []
        self.dfs(chars, "")
        return self.res