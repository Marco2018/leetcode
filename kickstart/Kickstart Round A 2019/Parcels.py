import copy
times=int(input())
for time in range(times):
    line=input()
    rc=[int(x) for x in line.strip().split()]
    r,c=rc[0],rc[1]
    office,nodes,visited,nodes2=[],[],[],[]
    for i in range(r):
        line=input()
        for j in range(len(line.strip())):
            if line[j]=="1":
                office.append([i,j])
                visited.append([i,j])
            else:
                nodes.append([i,j])
                nodes2.append([i,j])
    dp = [[float("inf") for i in range(c)] for j in range(r)]
    for off in office:
        dp[off[0]][off[1]]=0
    while nodes:
        temp_distance=float("inf")
        index_node=[-1,-1]
        for v in visited:
            for d in nodes:
                if dp[v[0]][v[1]]+abs(v[0]-d[0])+abs(v[1]-d[1])<temp_distance:
                    temp_distance=dp[v[0]][v[1]]+abs(v[0]-d[0])+abs(v[1]-d[1])
                    index_node=d
        if index_node!=[-1,-1]:
            dp[index_node[0]][index_node[1]]=temp_distance
            visited.append(index_node)
            nodes.remove(index_node)
        else:
            break
    index_i,index_j=0,0
    for i in range(r):
        for j in range(c):
            if dp[i][j]>dp[index_i][index_j]:
                index_i,index_j=i,j
    potential_list=[]
    for i in range(r):
        for j in range(c):
            if dp[i][j]==dp[index_i][index_j]:
                potential_list.append([i,j])
    nodes2_temp=copy.deepcopy(nodes2)
    office_temp=copy.deepcopy(office)
    res = float("inf")
    for [index_i,index_j] in potential_list:
        if [index_i,index_j] not in office:
            office.append([index_i,index_j])
        else:
            res=0
            break
        dp = [[float("inf") for i in range(c)] for j in range(r)]
        for off in office:
            dp[off[0]][off[1]]=0
        while nodes2:
            temp_distance=float("inf")
            for v in office:
                for d in nodes2:
                    if dp[v[0]][v[1]]+abs(v[0]-d[0])+abs(v[1]-d[1])<temp_distance:
                        temp_distance=dp[v[0]][v[1]]+abs(v[0]-d[0])+abs(v[1]-d[1])
                        index_node=d
            dp[index_node[0]][index_node[1]]=temp_distance
            office.append(index_node)
            nodes2.remove(index_node)
            res_temp=0
            for i in range(r):
                for j in range(c):
                    if dp[i][j]>res_temp:
                        res_temp=dp[i][j]
        nodes2 = copy.deepcopy(nodes2_temp)
        office = copy.deepcopy(office_temp)
        res=min(res,res_temp)
    print("Case #"+str(time+1)+": "+str(res))