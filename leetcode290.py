class Solution:    def wordPattern(self, pattern, str):        """        :type pattern: str        :type str: str        :rtype: bool        """        str=str.split()        if len(pattern)!=len(str):            return False        if pattern=="":            return True        dict,dict1={},{}        for i in range(len(str)):            if pattern[i] not in dict:                dict[pattern[i]]=str[i]            else:                if dict[pattern[i]]!=str[i]:                    return False            if str[i] not in dict1:                dict1[str[i]]=pattern[i]            else:                if dict1[str[i]]!=pattern[i]:                    return False        return Truepattern = "abba"str = "dog dog dog dog"s=Solution()print(s.wordPattern(pattern,str))