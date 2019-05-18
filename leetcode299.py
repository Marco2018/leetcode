from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a,b=0,0
        dict_num=defaultdict(int)
        for i in range(len(secret)):
            if guess[i]==secret[i]:
                a+=1
            else:
                dict_num[secret[i]]+=1
        for i in range(len(secret)):
            if guess[i]!=secret[i] and dict_num[guess[i]]>0:
                b+=1
                dict_num[guess[i]]-=1
        return str(a)+"A"+str(b)+"B"
		
Runtime: 40 ms, faster than 98.94% of Python3 online submissions for Bulls and Cows.