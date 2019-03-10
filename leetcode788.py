class Solution:
    def rotatedDigits(self, N):
        def isrotated(str1):
            n=len(str1)
            index=0
            set1=['1','0','2','5','6','8','9']
            set2=['2','5','6','9']
            for i in range(n):
                if str1[i] not in set1:
                    return 0
                if str1[i] in set2:
                   index=1
            if index==1:
                return 1
            else:
                return 0
        count=0
        for j in range(1,N+1):
            count+=isrotated(str(j))
        return count

solution=Solution()
n=2
print(solution.rotatedDigits(n))
