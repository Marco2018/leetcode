class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n=len(S)
        if n==0:
            return [0]
        arr,left,right=[],0,n
        for i in range(n):
            if S[i]=="I":
                arr.append(left)
                left+=1
            if S[i]=="D":
                arr.append(right)
                right-=1
        arr.append(left)
        return arr
s1=Solution()
A=["ift","efd","dnete","tef","fdn"]
print(s1.shortestSuperstring(A))
