def longestCommonPrefix(strs):
    n = len(strs)
    if n == 0:
        return ""
    str = ""
    index = 10000
    for k in range(n):
        if len(strs[k]) < index:
            index = len(strs[k])
    for j in range(index):
        word = strs[0][j]
        for i in range(n):
            if strs[i][j] != word:
                return str
        str = strs[0][:j+1:]
    return str


str=["a"]
print(longestCommonPrefix(str))
