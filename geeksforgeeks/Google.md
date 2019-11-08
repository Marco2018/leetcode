### Google

##### Easy Level

Find all triplets with zero sum

Given an array of distinct elements. The task is to find triplets in array whose sum is zero.

**Examples :**

```
Input : arr[] = {0, -1, 2, -3, 1}
Output : 0 -1 1
         2 -3 1

Input : arr[] = {1, -2, 1, 0, 5}
Output : 1 -2  1
```

**Method 1 (Simple : O(n3))**

```python
def findTriplets(arr, n): 
  
    found = True
    for i in range(0, n-2): 
        for j in range(i+1, n-1): 
            for k in range(j+1, n): 
                if (arr[i] + arr[j] + arr[k] == 0): 
                    print(arr[i], arr[j], arr[k]) 
                    found = True
      
              
    # If no triplet with 0 sum  
    # found in array 
    if (found == False): 
        print(" not exist ") 
  
# Driver code 
arr = [0, -1, 2, -3, 1] 
n = len(arr) 
findTriplets(arr, n) 
```

**Method 2 (Hashing : O(n2))**

```python
def findTriplets(arr, n): 
    found = False
    for i in range(n - 1): 
  
        # Find all pairs with sum  
        # equals to "-arr[i]"  
        s = set() 
        for j in range(i + 1, n): 
            x = -(arr[i] + arr[j]) 
            if x in s: 
                print(x, arr[i], arr[j]) 
                found = True
            else: 
                s.add(arr[j]) 
    if found == False: 
        print("No Triplet Found") 
```

**Method 3 (Sorting : O(n2))**
The above method requires extra space. We can solve in O(1) extra space. The idea is based on method 2 of [this](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/) post.

```python
# function to print triplets with 0 sum 
def findTriplets(arr, n): 
    found = False  
    # sort array elements 
    arr.sort() 
    for i in range(0, n-1):     
        # initialize left and right 
        l = i + 1
        r = n - 1
        x = arr[i] 
        while (l < r): 
          
            if (x + arr[l] + arr[r] == 0): 
                # print elements if it's sum is zero 
                print(x, arr[l], arr[r]) 
                l+=1
                r-=1
                found = True
              
            # If sum of three elements is less 
            # than zero then increment in left 
            elif (x + arr[l] + arr[r] < 0): 
                l+=1
            # if sum is greater than zero than 
            # decrement in right side 
            else: 
                r-=1       
    if (found == False): 
        print(" No Triplet Found") 
```



Generate all binary strings from given pattern

recursion

```python
# character by 0 or 1 
def _print(temp, string):
    if not string:
        print(temp)
        return
    if string[0] == "?":
        _print(temp+"0", string[1:])
        _print(temp+"1", string[1:])
    else:
        _print(temp+string[0], string[1:])
    return


if __name__ == "__main__":
    string = "1??0?101"
    _print("", string)
```

```python
# character by 0 or 1 
def _print(string, index): 
    if index == len(string): 
        print(''.join(string)) 
        return
  
    if string[index] == "?": 
  
        # replace '?' by '0' and recurse 
        string[index] = '0'
        _print(string, index + 1) 
  
        # replace '?' by '1' and recurse 
        string[index] = '1'
        _print(string, index + 1) 
  
        # NOTE: Need to backtrack as string 
        # is passed by reference to the 
        # function 
        string[index] = '?'
    else: 
        _print(string, index + 1) 
  
# Driver code 
if __name__ == "__main__": 
  
    string = "1??0?101"
    string = list(string) 
    _print(string, 0) 
  
```

记得recursion讲？改回来



Count of strings that can be formed using a, b and c under given constraints

Given a length n, count the number of strings of length n that can be made using ‘a’, ‘b’ and ‘c’ with at-most one ‘b’ and two ‘c’s allowed.

**Examples :**

```
Input : n = 3 
Output : 19 
Below strings follow given constraints:
aaa aab aac aba abc aca acb acc baa
bac bca bcc caa cab cac cba cbc cca ccb 

Input  : n = 4
Output : 39
```

A **simple solution** is to recursively count all possible combination

```python
def countStr(n, bCount, cCount): 
  
    # Base cases 
    if (bCount < 0 or cCount < 0): 
        return 0
    if (n == 0) : 
        return 1
    if (bCount == 0 and cCount == 0): 
        return 1
  
    # Three cases, we choose, a or b or c 
    # In all three cases n decreases by 1. 
    res = countStr(n - 1, bCount, cCount) 
    res += countStr(n - 1, bCount - 1, cCount) 
    res += countStr(n - 1, bCount, cCount - 1) 
  
    return res 
  
# Driver code 
if __name__ =="__main__": 
    n = 3 # Total number of characters 
    print(countStr(n, 1, 2))
```

上述中存在大量重复的情况

使用memorization

```python
def countStr(dp, n, bCount, cCount):
    # Base cases
    if (bCount < 0 or cCount < 0):
        return 0
    if (n == 0):
        return 1
    if (bCount == 0 and cCount == 0):
        return 1
    if dp[n][bCount][cCount] != -1:
        return dp[n][bCount][cCount]
    # Three cases, we choose, a or b or c
    # In all three cases n decreases by 1.
    res = countStr(dp, n - 1, bCount, cCount)
    res += countStr(dp, n - 1, bCount - 1, cCount)
    res += countStr(dp, n - 1, bCount, cCount - 1)
    dp[n][bCount][cCount] = res
    return res


# Driver code
if __name__ == "__main__":
    n = 3  # Total number of characters
    dp = [[[-1 for i in range(3)] for j in range(2)] for k in range(n+1)]
    print(countStr(dp, n, 1, 2))
```



Find largest word in dictionary by deleting some characters of given string

Giving a dictionary and a string ‘str’, find the longest string in dictionary which can be formed by deleting some characters of the given ‘str’.

Examples:

```
Input : dict = {"ale", "apple", "monkey", "plea"}   
        str = "abpcplea"  
Output : apple 

Input  : dict = {"pintu", "geeksfor", "geeksgeeks", 
                                        " forgeek"} 
         str = "geeksforgeeks"
Output : geeksgeeks
```

```python
def isSubSequence(str1, str2): 
  
    m = len(str1); 
    n = len(str2); 
  
    j = 0; # For index of str1 (or subsequence 
  
    # Traverse str2 and str1, and compare current 
    # character of str2 with first unmatched char 
    # of str1, if matched then move ahead in str1 
    i = 0; 
    while (i < n and j < m): 
        if (str1[j] == str2[i]): 
            j += 1; 
        i += 1; 
  
    # If all characters of str1 were found in str2 
    return (j == m); 
  
# Returns the longest string in dictionary which is a 
# subsequence of str. 
def findLongestString(dict1, str1): 
    result = ""; 
    length = 0; 
  
    # Traverse through all words of dictionary 
    for word in dict1: 
          
        # If current word is subsequence of str and is largest 
        # such word so far. 
        if (length < len(word) and isSubSequence(word, str1)): 
            result = word; 
            length = len(word); 
  
    # Return longest string 
    return result; 
  
# Driver program to test above function 
  
dict1 = ["ale", "apple", "monkey", "plea"]; 
str1 = "abpcplea" ; 
print(findLongestString(dict1, str1));
```

isSubSequence函数用来判断str1是否是str2的substring的方法可以学习



Find subarray with given sum | Set 1 (Nonnegative Numbers)

Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number.

**Examples :**

> **Input**: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
> **Ouptut**: Sum found between indexes 2 and 4
>
> **Input**: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
> **Ouptut**: Sum found between indexes 1 and 4
>
> **Input**: arr[] = {1, 4}, sum = 0
> **Output**: No subarray found

```python
def subArraySum(arr, sum):
    n = len(arr)
    sums = [0 for i in range(n+1)]
    seen = {}
    seen[0] = 0
    for i in range(n):
        sums[i+1] = sums[i] + arr[i]
        seen[sums[i+1]] = i+1
        if sums[i+1] - sum in seen:
            return [seen[sums[i+1]-sum], i]

    return


# Driver code
if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    sum = 23
    print(subArraySum(arr, sum))
```



Flood fill Algorithm – how to implement fill() in paint?



In MS-Paint, when we take the brush to a pixel and click, the color of the region of that pixel is replaced with a new selected color. Following is the problem statement to do this task.
Given a 2D screen, location of a pixel in the screen and a color, replace color of the given pixel and all adjacent same colored pixels with the given color.

**Example:**

```
Input:
       screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 0, 1, 1, 0, 1, 1},
                      {1, 2, 2, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 2, 2, 0},
                      {1, 1, 1, 1, 1, 2, 1, 1},
                      {1, 1, 1, 1, 1, 2, 2, 1},
                      };
    x = 4, y = 4, newColor = 3
The values in the given 2D screen indicate colors of the pixels.
x and y are coordinates of the brush, newColor is the color that
should replace the previous color on screen[x][y] and all surrounding
pixels with same color.

Output:
Screen should be changed to following.
       screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 0, 1, 1, 0, 1, 1},
                      {1, 3, 3, 3, 3, 0, 1, 0},
                      {1, 1, 1, 3, 3, 0, 1, 0},
                      {1, 1, 1, 3, 3, 3, 3, 0},
                      {1, 1, 1, 1, 1, 3, 1, 1},
                      {1, 1, 1, 1, 1, 3, 3, 1},
                      };
```

```python
def floodFillUtil(screen, x, y, prevC, newC): 
      
    # Base cases 
    if (x < 0 or x >= M or y < 0 or 
        y >= N or screen[x][y] != prevC or 
        screen[x][y] == newC): 
        return
  
    # Replace the color at (x, y) 
    screen[x][y] = newC 
  
    # Recur for north, east, south and west 
    floodFillUtil(screen, x + 1, y, prevC, newC) 
    floodFillUtil(screen, x - 1, y, prevC, newC) 
    floodFillUtil(screen, x, y + 1, prevC, newC) 
    floodFillUtil(screen, x, y - 1, prevC, newC) 
  
# It mainly finds the previous color on (x, y) and  
# calls floodFillUtil()  
def floodFill(screen, x, y, newC): 
    prevC = screen[x][y] 
    floodFillUtil(screen, x, y, prevC, newC) 
  
# Driver Code 
screen = [[1, 1, 1, 1, 1, 1, 1, 1],  
          [1, 1, 1, 1, 1, 1, 0, 0],  
          [1, 0, 0, 1, 1, 0, 1, 1],  
          [1, 2, 2, 2, 2, 0, 1, 0],  
          [1, 1, 1, 2, 2, 0, 1, 0],  
          [1, 1, 1, 2, 2, 2, 2, 0],  
          [1, 1, 1, 1, 1, 2, 1, 1],  
          [1, 1, 1, 1, 1, 2, 2, 1]] 
  
x = 4
y = 4
newC = 3
floodFill(screen, x, y, newC) 
  
print ("Updated screen after call to floodFill:") 
for i in range(M): 
    for j in range(N): 
        print(screen[i][j], end = ' ') 
    print() 
```



Meta Strings (Check if two strings can become same after a swap in one string)

Given two strings, the task is to check whether these strings are meta strings or not. Meta strings are the strings which can be made equal by exactly one swap in any of the strings. Equal string are not considered here as Meta strings.

Examples:

```
Input : str1 = "geeks" 
        str2 = "keegs"
Output : Yes
By just swapping 'k' and 'g' in any of string, 
both will become same.

Input : str1 = "rsting"
        str2 = "string
Output : No

Input :  str1 = "Converse"
         str2 = "Conserve"
```

```python
def areMetaStrings( str1, str2) : 
    len1 = len(str1) 
    len2 = len(str2) 
        
    # Return false if both are not of equal length 
    if (len1 != len2) : 
        return False
        
    # To store indexes of previously mismatched 
    # characters 
    prev = -1
    curr = -1
        
    count = 0 
    i = 0
    while i < len1 : 
              
        # If current character doesn't match 
        if (str1[i] != str2[i] ) : 
         
        # Count number of unmatched character 
            count = count + 1
        
            # If unmatched are greater than 2, 
            # then return false 
            if (count > 2) : 
                return False
        
            # Store both unmatched characters of 
            # both strings 
            prev = curr 
            curr = i 
              
        i = i + 1
        
    # Check if previous unmatched of string1 
    # is equal to curr unmatched of string2 
    # and also check for curr unmatched character, 
    # if both are same, then return true 
    return (count == 2 and str1[prev] == str2[curr] 
               and str1[curr] == str2[prev]) 
      
# Driver method 
str1 = "converse"
str2 = "conserve"
if ( areMetaStrings(str1,str2) ) : 
     print "Yes" 
else: 
    print "No"
```

统计是不是两个 同时换一下是不是一样



Print all Jumping Numbers smaller than or equal to a given value

A number is called as a Jumping Number if all adjacent digits in it differ by 1. The difference between ‘9’ and ‘0’ is not considered as 1.
All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

Given a positive number x, print all Jumping Numbers smaller than or equal to x. The numbers can be printed in any order.

Example:

```
Input: x = 20
Output:  0 1 2 3 4 5 6 7 8 9 10 12

Input: x = 105
Output:  0 1 2 3 4 5 6 7 8 9 10 12
         21 23 32 34 43 45 54 56 65
         67 76 78 87 89 98 101

Note: Order of output doesn't matter, 
i.e. numbers can be printed in any order
```

```python
def dfs(temp, x):
    if int(temp) > x:
        return
    if temp:
        print(temp, end=' ')
    last_num = int(temp[-1])
    if last_num == 0:
        dfs(temp + "1", x)
    elif last_num == 9:
        dfs(temp + "8", x)
    else:
        dfs(temp + str(last_num-1), x)
        dfs(temp + str(last_num+1), x)
    return

# a positive number x
def printJumping(x):
    print(str(0), end=' ')
    for i in range(1, 10):
        temp = str(i)
        dfs(temp, x)


    # Driver code
if __name__ == "__main__":
    x = 40
    printJumping(x)
```

DFS



Sum of all the numbers that are formed from root to leaf paths

Given a binary tree, where every node value is a Digit from 1-9 .Find the sum of all the numbers which are formed from root to leaf paths.

For example consider the following Binary Tree.

```
           6
       /      \
     3          5
   /   \          \
  2     5          4  
      /   \
     7     4
  There are 4 leaves, hence 4 root to leaf paths:
   Path                    Number
  6->3->2                   632
  6->3->5->7               6357
  6->3->5->4               6354
  6->5>4                    654   
Answer = 632 + 6357 + 6354 + 654 = 13997 
```

```python
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def treePathsSumUtil(root, path, res):
    # Base Case
    if root.left == None and root.right == None:
        if path:
            res.append(int(path))
        return
    if root.left:
        treePathsSumUtil(root.left, path + str(root.left.data), res)
    if root.right:
        treePathsSumUtil(root.right, path + str(root.right.data), res)
    return


# A wrapper function over treePathSumUtil()
def treePathsSum(root):
    # Pass the initial value as 0 as ther is nothing above root
    res = []
    if not root:
        return 0
    treePathsSumUtil(root, str(root.data), res)
    return sum(res)


# Driver function to test above function
root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
print (treePathsSum(root))
```

