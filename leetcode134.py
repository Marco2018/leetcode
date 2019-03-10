class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n=len(gas)
        cha=[0 for i in range(n)]
        for i in range(n):
            cha[i]=gas[i]-cost[i]
        for i in range(n):
            res,start=0,i
            res+=cha[i]
            start+=1
            while res>=0:
                if start>=n:
                    start-=n
                if start==i:
                    return i
                res+=cha[start]
                start+=1
        return -1
s1=Solution()
gas  = [3,1,1]
cost = [1,2,2]
print(s1.canCompleteCircuit(gas,cost))

def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
        return -1
    position = 0
    balance = 0 # current tank balance
    for i in range(len(gas)):
        balance += gas[i] - cost[i] # update balance
        if balance < 0: # balance drops to negative, reset the start position
            balance = 0
            position = i+1
    return position