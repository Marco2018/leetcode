if __name__=="__main__":
    line=input()
    nums=[int(x) for x in line.strip().split()]
    n,s,l=nums[0],nums[1],nums[2]
    count=1+(l-s)//(s+1)
    if count%13==0:
        count-=1
    res=(n+count-1)//count
    if n%count!=0 and (n%count==count-1 and (n%count)%13==0) or (res==1 and n%13==0):#两种情况一种是只有1个CD且n%13==0 或者是多张CD但是除了一张数量被13整除的且还有一首空余量的CD外，其余每张CD都满且数量是13n+1
        res+=1
    print(res)