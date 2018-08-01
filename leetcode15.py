def threeSum(nums):
    res=[]
    n=len(nums)
    if n<3:
        return []
    nums.sort()
    for i in range(n-2):
        j=i+1
        k=n-1
        if i>0 and nums[i]==nums[i-1]:
            continue
        while j<k:
            sum=nums[i]+nums[j]+nums[k]
            if sum==0:
                res.append((nums[i],nums[j],nums[k]))
                k=k-1
                j=j+1
            elif sum>0:
                k=k-1
            else:
                j=j+1
    return list(set(res))

nums = [0,0,0]
print(threeSum(nums))