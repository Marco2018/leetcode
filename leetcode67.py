class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lista=list(a)
        listb=list(b)
        lista.reverse()
        listb.reverse()
        res=""
        carry=0
        n=min(len(lista),len(listb))
        for i in range(n):
            temp=int(lista[i])+int(listb[i])+carry
            if temp>=2:
                temp-=2
                carry=1
            else:
                carry=0
            res=res+str(temp)
        if len(lista)>n:
            for j in range(i+1,len(lista)):
                temp=int(lista[j])+carry
                if temp>=2:
                    temp-=2
                    carry=1
                else:
                    carry=0
                res = res + str(temp)
        if len(listb) > n:
            for k in range(i+1, len(listb)):
                temp = int(listb[k]) + carry
                if temp >= 2:
                    temp -= 2
                    carry = 1
                else:
                    carry = 0
                res = res + str(temp)
        if carry!=0:
            res = res + str(carry)
        b=list(res)
        b.reverse()
        s=""
        for i in b:
            s=s+i
        return s
object1=Solution()
a = "101111"
b = "10"
print(Solution.addBinary(object1,a,b))