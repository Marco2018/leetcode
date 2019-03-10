class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        if n <= 1:
            return 0
        ones=[]
        for i in range(n):
            if seats[i]==1:
                ones.append(i)
        res_length =  -1
        if len(ones)==1:
            return max(ones[0],n-1-ones[0])
        for i in range(1,len(ones)):
            if int((ones[i]-ones[i-1])/2)>res_length:
                res_length=int((ones[i]-ones[i-1])/2)
        res_length=max(res_length,ones[0],n-1-ones[-1])
        return res_length
s1=Solution()
print(s1.maxDistToClosest([1,0,0,0,1,1,0,0,0,0,0]))