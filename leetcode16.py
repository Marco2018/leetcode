def threeSumClosest(nums, target):
    n=len(nums)
    if n<3:
        return 0
    index=abs(nums[0]+nums[1]+nums[2]-target)
    val=nums[0]+nums[1]+nums[2]
    nums.sort()
    for i in range(n-2):
        left=i+1
        right=len(nums)-1
        while right>left:
            sum = nums[i] + nums[left] + nums[right]
            if abs(sum-target)==0:
                return sum
            elif abs(sum-target)<index:
                index=abs(nums[i]+nums[left]+nums[right]-target)
                val=nums[i]+nums[left]+nums[right]
            if sum-target>0:
                right=right-1
            if sum-target<0:
                left=left+1
    return val