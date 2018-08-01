class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict1={}
        dict2={}
        for i in range(len(ransomNote)):
            if ransomNote[i] not in dict1:
                dict1[ransomNote[i]]=1
            else:
                dict1[ransomNote[i]]+=1
        for j in range(len(magazine)):
            if magazine[j] not in dict2:
                dict2[magazine[j]]=1
            else:
                dict2[magazine[j]]+=1
        for key,value in dict1.items():
            if key not in dict2 or value>dict2[key]:
                return False
        return True
solution=Solution()
ransomNote = "aaa"
magazine= "ab"
print(solution.canConstruct(ransomNote , magazine))



