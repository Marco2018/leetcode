import sys
def dfs(map1,isvisited,i,j):
    isvisited[i][j]=1
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for k in range(4):
        if 0<=i+dx[k]<4 and 0<=j+dy[k]<5:
            if map1[i+dx[k]][j+dy[k]]==1 and isvisited[i+dx[k]][j+dy[k]]==0:
                dfs(map1,isvisited,i+dx[k],j+dy[k])
    return
if __name__ == "__main__":
    map1 = []
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        nums = [int(x) for x in list(line)]
        map1.append(nums)
    isvisited=[[0 for i in range(5)]for j in range(4)]
    count=0
    for i in range(4):
        for j in range(5):
            if map1[i][j]==1 and isvisited[i][j]==0:
                count+=1
                dfs(map1,isvisited,i,j)
    print(count)

# 岛屿的个数
#给一个01矩阵，求不同的岛屿的个数。

#0代表海，1代表岛，如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。

[
[1, 1, 0, 0, 0],
[0, 1, 0, 0, 1],
[0, 0, 0, 1, 1],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 1]
]
中有 3 个岛