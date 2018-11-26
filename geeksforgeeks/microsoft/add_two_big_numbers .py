class Solution(object):
    #no same number
    def add_number (self,arr1,arr2):
        n,m=len(arr1),len(arr2)
        if n==0:
            return arr2
        if m==0:
            return arr1
        if n<m:
            arr1=[0]*(m-n)+arr1
        if n>m:
            arr2=[0]*(n-m)+arr2
        carry,length=0,max(n,m)
        arr3=[]
        for i in range(length):
            temp=arr1[length-1-i]+arr2[length-1-i]+carry
            if temp>=10:
                carry=1
                temp-=10
            arr3=[temp]+arr3
        if carry:
            arr3=[carry]+arr3
        return arr3
s1=Solution()
arr1=[5,6,3]
arr2=[8,8,8]
print(s1.add_number (arr1,arr2))