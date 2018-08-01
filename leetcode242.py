class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1={}
        dict2={}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]]=1
            else:
                dict1[s[i]]+=1
        for j in range(len(t)):
            if t[j] not in dict2:
                dict2[t[j]]=1
            else:
                dict2[t[j]]+=1
        for key,value in dict1.items():
            if key not in dict2 or value!=dict2[key]:
                return False
        for key2,value2 in dict2.items():
            if key2 not in dict1 or value2!=dict1[key2]:
                return False
        return True
solution=Solution()
s = "a"
t = "ab"
print(solution.isAnagram(s , t))



