class Solution:
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def f(S):
            i=S.find('(')
            if i>0:
                s1=S[:i]+S[i+1:len(S)-1]*20
                return float(s1)
            else:
                return float(S)
            return
        return f(S)==f(T)
在python中：
>>> 0.9999999999999==1
False
>>> 0.999999999999999999999999999999999999999999==1
True

首先判断是否存在循环，否则直接利用float(s1)返回数值
如果存在循环则将循环拉长20倍 这样可以使得0.999999=1

当然这题的本意应该不是这样考察的
应该是两个string搭配两个指针
两个指针一起移动，如果数值不同返回False 直到移动到循环部分之后再继续二者循环部分的最小公倍数次后 返回True