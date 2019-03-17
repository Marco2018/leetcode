class Solution:
    def shipWithinDays(self, weights, D):
        capacity_left, capacity_right, n = max(weights), sum(weights), len(weights)
        while capacity_left < capacity_right:
            capacity = (capacity_left + capacity_right) // 2
            count, temp, i = 1, 0, 0
            while i < n:
                if capacity < temp + weights[i]:
                    temp = 0
                    count += 1
                else:
                    temp += weights[i]
                    i += 1
            if count > D:
                capacity_left = capacity + 1
            else:
                capacity_right = capacity
        return capacity_left


"""
class Solution:
    def shipWithinDays(self, weights,D):
        capacity,n=max(weights),len(weights)
        while True:
            count,temp,i,n_capacity=1,0,0,float("inf")
            while i<n:
                if capacity<temp+weights[i]:
                    n_capacity=min(n_capacity,temp+weights[i])
                    temp=0
                    count+=1
                else:
                    temp+=weights[i]
                    i+=1
            if count<=D:
                return capacity
            else:
                capacity=n_capacity
"""


s1=Solution()
weights=[1,2,3,4,5,6,7,8,9,10]
D=5
print(s1.shipWithinDays(weights,D))

