import string
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        lower=paragraph.lower()
        for c in string.punctuation:
            lower=lower.replace(c,"")
        p=lower.split(" ")
        words={}
        for word in p:
            if word not in banned:
                if word not in words:
                    words[word]=1
                else:
                    words[word]+=1
        for key,value in words.items():
            if value==max(words.values()):
                return key
solution=Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(solution.mostCommonWord(paragraph, banned))
'''
高阶低阶：
lower=paragraph.lower()

除去标点符号：
    for c in string.punctuation:
        lower=lower.replace(c,"")

split
p=lower.split(" ")

字典：
max(words.value()) #2
max(words.key()) #was
    for key,value in words.items():
        if value==max(words.values()):
            return key
# ball
'''


