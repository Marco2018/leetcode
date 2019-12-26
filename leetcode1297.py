import collections
class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        d,dd,n={},{},minSize-1
        for i in range(n):
            dd[s[i]]=dd.get(s[i],0)+1
        for i in range(len(s)-n):
            c,cc=s[i],s[i+n]
            dd[cc]=dd.get(cc,0)+1
            if len(dd)<=maxLetters:
                t=s[i:i+minSize]
                d[t]=d.get(t,0)+1
            dd[c]-=1
            if not dd[c]: del dd[c]
        return max(d.values() or [0])
        
sliding windows