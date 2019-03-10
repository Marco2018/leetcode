class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n=len(A)
        if n<3:
            return False
        if A[0]>=A[1]:
            return False
        for index in range(1,n-1):
            if A[index+1]==A[index]:
                return False
            elif A[index+1]>A[index]:
                continue
            else:
                break
        for i in range(index+1,n,1):
            if A[i]>=A[i-1]:
                return False
        return True
s1=Solution()
A=["ift","efd","dnete","tef","fdn"]
print(s1.shortestSuperstring(A))
