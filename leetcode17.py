class Solution:
    def letterCombinations(self,digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return []
        dict={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        return ["".join(s) for s in itertools.product(*[dict[dig] for dig in digits])]


str="234"
print(Solution.letterCombinations(str))

"""
import itertools
itertools.product()表示求笛卡尔积
list1 = ['a', 'b']
list2 = ['c', 'd']
for i in itertools.product(list1, list2):
    print i
('a', 'c')
('a', 'd')
('b', 'c')
('b', 'd')
但是如果不确定有几个list，则可以使用*解包
*[dict[dig] for dig in digits] 这一步相当于把[]中的多个list都解了出来
下一步使用itertools.product()，得到
('a', 'c')
('a', 'd')
('b', 'c')
('b', 'd')
使用"".join(s)将这些字母串起来
"""


class solution():
    def letter(self,str1):
        self.letters=["abc","def","ghi","jki","mno","pqrs","tuv","wxyz"]
        self.res=[]
        self.helper("",str1)
        return self.res
    def helper(self,temp,str1):
        if len(str1)==0:
            self.res.append(temp)
            return
        letters=self.letters[ord(str1[0])-ord("2")]
        for letter in letters:
            self.helper(temp+letter,str1[1::])
        return