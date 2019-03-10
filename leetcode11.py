def maxArea(height):
    area=maxarea=0
    n=len(height)
    j=n-1
    i=0
    while i<j:
        area=min(height[i],height[j])*(j-i)
        if area>maxarea:
            maxarea=area
        if height[i]>height[j]:
            j=j-1
        else:
            i=i+1
    return maxarea