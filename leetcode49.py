class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans,res,result=[],{},[]
        for i in range(len(strs)):
            a=list(strs[i])
            a.sort()
            ans.append("".join(a))
        for j in range(len(ans)):
            if ans[j] not in res:
                res[ans[j]]=[]
            res[ans[j]].append(strs[j])
        for key in res:
            result.append(res[key])
        return result



object1=Solution()
str1= ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution.groupAnagrams(object1,str1))

#dict 中的结构必须要是hashable
