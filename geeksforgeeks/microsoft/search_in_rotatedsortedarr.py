class Solution(object):
    #no same number
    def search (self,arr,s):
        n=len(arr)
        if n==0:
            return
        left,right=0,n-1
        while left<=right:
            mid=int((left+right)/2)
            if arr[mid]==key:
                return mid
            #left array is sorted
            if arr[mid]>arr[left]:
                if key>arr[left] and key<=arr[mid]:
                    right=mid-1
                else:
                    left=mid+1
            #right array is sorted
            else:
                if arr[mid]<key and key<arr[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
s1=Solution()
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 6
print(s1.search (arr,key))