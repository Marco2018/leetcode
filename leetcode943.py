class Solution:
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        # construct a directed graph
        #   node i => A[i]
        #   weights are represented as an adjacency matrix:
        #   shared[i][j] => length saved by concatenating A[i] and A[j]
        n = len(A)
        shared = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(min(len(A[i]), len(A[j])), -1, -1):
                    if A[i][-k:] == A[j][:k]:
                        shared[i][j] = k
                        break

        # The problem becomes finding the shortest path that visits all nodes exactly once.
        # Brute force DFS would take O(n!) time.
        # A DP solution costs O(n^2 2^n) time.
        #
        # Let's consider integer from 0 to 2^n - 1.
        # Each i contains 0-n 1 bits. Hence each i selects a unique set of strings in A.
        # Let's denote set(i) => {A[j] | j-th bit of i is 1}
        # dp[i][k] => shortest superstring of set(i) ending with A[k]
        #
        # e.g.
        #   if i = 5 i.e. 110 in binary. dp[5][k] considers superstring of A[2] and A[1].
        #   dp[5][1] => the shortest superstring of {A[2], A[1]} ending with A[1].
        #   For this simple case dp[5][1] = concatenate(A[2], A[1])
        dp = [[''] * 12 for _ in range(1 << 12)]
        for i in range(1 << n):
            for k in range(n):
                # skip if A[k] is not in set(i)
                if not (i & (1 << k)):
                    continue
                # if set(i) == {A[k]}
                if i == 1 << k:
                    dp[i][k] = A[k]
                    continue
                for j in range(n):
                    if j == k:
                        continue
                    if i & (1 << j):
                        # the shortest superstring if we remove A[k] from the set(i)
                        s = dp[i ^ (1 << k)][j]
                        s += A[k][shared[j][k]:]
                        if dp[i][k] == '' or len(s) < len(dp[i][k]):
                            dp[i][k] = s

        min_len = float('inf')
        result = ''

        # find the shortest superstring of all candidates ending with different string
        for i in range(n):
            s = dp[(1 << n) - 1][i]
            if len(s) < min_len:
                min_len, result = len(s), s
        return result
class Solution(object):
    def shortestSuperstring(self, A):

        def findsim(str1,str2):
            n1=min(len(str1),len(str2))
            for i in range(n1,-1,-1):
                if str1[-i:]==str2[:i]:
                    return i
            return 0
        def merge(index1,index2,x):
            str1, str2 = A[index1], A[index2]
            new_str=str1+str2[x:]
            return new_str
        n=len(A)
        if n==0:
            return ""
        while len(A)>1:
            maxlenth, index1, index2 = -1, 0, 0
            for i in range(len(A)):
                for j in range(len(A)):
                    if i!=j:
                        temp=findsim(A[i],A[j])
                        if temp>maxlenth:
                            maxlenth = temp
                            index1 = i
                            index2 = j
            new_str=merge(index1,index2,maxlenth)
            item1,item2=A[index1],A[index2]
            A.remove(item1)
            A.remove(item2)
            A.append(new_str)
        return A[0]
"""
import itertools
class Solution(object):
    def shortestSuperstring(self, A):
        def overlap(w1, w2):
            n1, n2 = len(w1), len(w2)
            ans = 0
            s = ''
            for i in range(1, min(n1, n2) + 1):
                if w1[-i:] == w2[:i]:
                    if ans < i:
                        ans = i
                        s = w1 + w2[i:]
            for i in range(1, min(n1, n2) + 1):
                if w2[-i:] == w1[:i]:
                    if ans < i:
                        ans = i
                        s = w2 + w1[i:]
            return (ans, s) if ans > 0 else (ans, w1 + w2)
        A = set(A)
        while len(A) != 1:
            l, s = float('-inf'), None
            x, y = None, None
            # print(A)
            for a, b in itertools.combinations(A, 2):
                # print(a, b)
                l_temp, s_temp = overlap(a, b)
                if l_temp > l:
                    l = l_temp
                    s = s_temp
                    x, y = a, b
            # print(a, b, s)
            A.remove(x)
            A.remove(y)
            A.add(s)
            # print(s)
        return A.pop()
"""
s1=Solution()
A=["ift","efd","dnete","tef","fdn"]
print(s1.shortestSuperstring(A))
