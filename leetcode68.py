class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res,temps,num_spaces=[],[],[]
        nums=[0 for i in range(len(words))]
        for i in range(len(words)):
            nums[i]=len(words[i])
        i=0
        while i<len(words):
            start = i
            temp_len=maxWidth-nums[i]
            i+=1
            while i<len(words) and temp_len>=len(words[i])+1:
                temp_len-=(len(words[i])+1)
                i+=1
            temps.append(words[start:i])
            num_spaces.append(temp_len+i-start-1)
        for i in range(len(temps)-1):
            string=""
            n=len(temps[i])
            number_spaces=num_spaces[i]
            string += temps[i][0]
            if n>1:
                average=int(number_spaces/(n-1))
                for j in range(1,len(temps[i]),1):
                    if j<=number_spaces-(n-1)*average:
                        string+=" "*(average+1)
                    else:
                        string+=" "*average
                    string+=temps[i][j]
            else:
                string+=" "*(maxWidth-len(string))
            res.append(string)
        string=temps[-1][0]
        for i in range(1,len(temps[-1]),1):
            string=string+" "+temps[-1][i]
        string+=" "*(maxWidth-len(string))
        res.append(string)
        return res
s1=Solution()
words =["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(s1.fullJustify(words,maxWidth))