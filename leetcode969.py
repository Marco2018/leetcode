class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def find(A,x):
            for i in range(len(A)):
                if A[i]==x:
                    return i
            return -1
        res,n=[],len(A)
        for i in range(n-1,-1,-1):
            if A[i]!=i+1:
                index=find(A,i+1)
                A=A[:index+1][::-1]+A[index+1:]
                A=A[:i+1][::-1]+A[i+1:]
                if index+1>1:
                    res.append(index+1)
                if i+1>1:
                    res.append(i+1)
        return res
		
不止有一种解法，由于只能翻转前k个pancake
很自然地想到先把最后面的pancake依次按照顺序放好
先从后往前开始检查，如果不对则找要交换的数在哪个位置(index)
通过将前index个pancake交换的方式将这个放到最前面，然后再n个翻转