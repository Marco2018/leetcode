class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A=="" and B=="":
            return True
        n=len(A)
        for i in range(n):
            C=A[1:]+A[0]
            A=C
            if B==A:
                return True
        return False
solution=Solution()
A = 'abcde'
B = 'cdeab'
print(solution.rotateString(A,B))
