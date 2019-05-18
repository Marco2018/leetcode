class Solution:
    def myAtoi(self,str1):
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        n,result,i,sign=len(str1),0,0,1
        while i<n and str1[i]==" ":
            i+=1
        if i<n and str1[i]=="-":
            sign=-1
            i+=1
        elif i<n and str1[i]=="+":
            sign=1
            i+=1
        while i<n and "0"<=str1[i]<="9":
            result=result*10+ord(str1[i])-ord("0")
            i+=1
        result=sign*result
        if result<MIN_INT: 
            return MIN_INT
        elif result>MAX_INT:
            return MAX_INT
        else:
            return result
        
python中没有MAX_INT MIN_INT这样的常量
