class Solution(object):    def longestPalindrome(self, s):        """        :type s: str        :rtype: str        """        n=len(s)        if n==0:            return ""        num,i=1,0        res=s[0]        while i<n-1:            pivot=i+1            while pivot<n and s[i]==s[pivot]:                pivot+=1            temp=s[i:pivot] #temp str            left,right=i-1,pivot            while left>=0 and right<=n-1:                if s[left]==s[right]:                    temp=s[left]+temp+s[right]                else:                    break                left-=1                right+=1            i=pivot            if len(temp)>num:                num,res=len(temp),temp        return resinput="caba"s=Solution()print(s.longestPalindrome(input))