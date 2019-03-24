times=int(input())
for time in range(times):
    line=input()
    np=[int(x) for x in line.strip().split()]
    n,p=np[0],np[1]
    line=input()
    nums=[int(x) for x in line.strip().split()]
    nums.sort(reverse=True)
    res=0
    for i in range(p):
        res+=nums[0]-nums[i]
    prev=res
    for i in range(1,n-p+1):
        temp_sum=prev-(p-1)*(nums[i-1]-nums[i])+nums[i]-nums[i+p-1]
        prev=temp_sum
        res=min(temp_sum,res)
        if res==0:
            break
    print("Case #"+str(time+1)+": "+str(res))
