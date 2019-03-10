class Node:
    def __init__(self,value):
        self.left=None
        self.val=value
        self.right=None
class Solution(object):
    # 4组 0-255 不能0开头
    def validateIP_address(self,s):
        nums_str=s.split(".")
        if len(nums_str)!=4:
            return False
        for i in range(4):
            if nums_str[i][0]<="0" or nums_str[i][0]>"9":
                return False
            for j in range(1,len(nums_str[i])):
                if nums_str[i][j]<"0" or nums_str[i][j]>"9":
                    return False
            if int(nums_str[i])<0 or int(nums_str[i])>255:
                return False
        return True

s1=Solution()
print(s1.validateIP_address("10.255.1.2"))