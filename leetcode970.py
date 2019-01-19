class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        x_nums,nums,set1=[],[],set()
        i=0
        if x==1:
            x_nums.append(1)
        else:
            while x**i<=bound:
                x_nums.append(x**i)
                i+=1
        i=0
        if y==1:
            for item in x_nums:
                if item+1 not in set1 and item +1<=bound:
                    nums.append(item+1)
                    set1.add(item+1)
        else:
            while y**i<=bound:
                for item in x_nums:
                    if y**i+item<=bound and y**i+item not in set1:
                        nums.append(y**i+item)
                        set1.add(y**i+item)
                i+=1
        return nums
要考虑x,y是否为1
如果xy是1的话y**i始终为 1
