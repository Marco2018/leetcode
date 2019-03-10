def myAtoi(str1):
    n=len(str1)
    i=0
    isfirst=isminus=isfirstword=0
    num=0
    while i<n:
        if str1[i]==" " and isfirstblank==0:
           i=i+1
           continue
        else:
            isfirstblank=1
            if isfirstword==0:
                if str1[i]>="0" and str1[i]<="9" or str1[i]=="+" or str1[i]=="-":
                    isfirstword=1
                    if str1[i]=="-":
                        isminus=1
                    if str1[i]>="0" and str1[i]<="9":
                        num=num*10
                        num=num+ord(str1[i])-ord('0')
                else:
                    break
            else:
                if str1[i]>="0" and str1[i]<="9":
                    num=num*10
                    num=num+ord(str1[i])-ord('0')
                else:
                    break
        i=i+1
    if isminus==1:
        num=-num
    if num>2**31-1:
        num=2**31-1
    elif num<-2**31:
        num=-2**31
    return  num

string = "-91283472332"
print(myAtoi(string))
