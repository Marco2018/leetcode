class Solution:
    def sumSubarrayMins(self, A):
        res = 0
        stack = []  #  non-decreasing
        A = [float('-inf')] + A + [float('-inf')]
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                cur = stack.pop()
                res += A[cur] * (i - cur) * (cur - stack[-1])
            stack.append(i)
        return res % (10**9 + 7)
ss=Solution()
print(ss.sumSubarrayMins([19,19,62,66]))

"""
class Solution:
    def sumSubarrayMins(self, A):
        res,n=0,len(A)
        left,right=[0 for i in range(n)],[0 for i in range(n)]
        stack=[0]
        left[0]=1
        for i in range(1,n):
            if A[i]>=A[stack[-1]]:
                stack.append(i)
                for j in range(len(stack)):
                    left[stack[j]]+=1
            else:
                while stack and A[i]<A[stack[-1]]:
                    stack.pop()
                stack.append(i)
                for j in range(len(stack)):
                    left[stack[j]] += 1
        stack = [n-1]
        right[n-1] = 1
        for i in range(n-2,-1,-1):
            if A[i] > A[stack[-1]]:
                stack.append(i)
                for j in range(len(stack)):
                    right[stack[j]] += 1
            else:
                while stack and A[i] <= A[stack[-1]]:
                    stack.pop()
                stack.append(i)
                for j in range(len(stack)):
                    right[stack[j]] += 1
        for i in range(n):
            res+=A[i]*left[i]*right[i]
        return res%(10**9 + 7)
"""
