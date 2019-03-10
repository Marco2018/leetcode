# leetcode
leetcode
350：
求nums1 和nums2的重叠：
如果可以重复，可以用dict求出每个元素的个数
```
for i in range(len(nums2)):
            if nums2[i] in dict:
                dict[nums2[i]]+=1
            else:
                dict[nums2[i]]=1
        for i in range(len(nums1)):
            if nums1[i] in dict:
                if dict[nums1[i]]>0:
                    ans.append(nums1[i])
                    dict[nums1[i]]-=1
```

hashtable

count primes:
```
前n个数有多少个质数
对每个数进行判断肯定超时
s = [1] * n
s[0] = 0
s[1] = 0
if s[i] == 1:
# Use slicing to speed up the zero assignments.
    s[i * i:n:i] = [0] * int((n - 1 - i * i) / i + 1)
#将质数的倍数都去掉
return sum(s)
```

string:
```
s.split()和s.split(" ")

string与list的切片 不用考虑越界的问题
for i in range(0,n,2*k):
    list1[i:i+k]=reversed(list1[i:i+k])

>>> a[4:5]
[]
>>> s="123"
>>> s[3:4]
''
不用考虑i+k>n
```
