class Solution:    def sortArrayByParityII(self, A):        """        :type A: List[int]        :rtype: List[int]        """        n=len(A)        if n==0:            return []        odd=even=0        while True:            while odd<n:                if A[odd]%2==1 and odd%2==0:                    break                odd+=1            while even<n:                if A[even]%2==0 and even%2==1:                    break                even+=1            if odd<n and even<n:                A[odd],A[even]=A[even],A[odd]            else:                break        return A