class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        changing_dollars=[0,0]
        for i in range(len(bills)):
            change=bills[i]-5
            if change==15:
                if changing_dollars[1]>0 and changing_dollars[0]>0:
                    changing_dollars[0]-=1
                    changing_dollars[1]-=1
                elif changing_dollars[0]>2:
                    changing_dollars[0] -= 3
                else:
                    return False
            elif change==5:
                if changing_dollars[0]>0:
                    changing_dollars[0]-=1
                    changing_dollars[1]+=1
                else:
                    return False
            else:
                changing_dollars[0] += 1
        return True
solution=Solution()
list=[5,5,10,10,20]
print(solution.lemonadeChange(list))
