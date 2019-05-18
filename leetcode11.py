def maxArea(height):
    maxarea,n,i,j=0,len(height),0,n-1
    while i<j:
        area=min(height[i],height[j])*(j-i)
        maxarea=max(area,maxarea)
        if height[i]>height[j]:
            j=j-1
        else:
            i=i+1
    return maxarea