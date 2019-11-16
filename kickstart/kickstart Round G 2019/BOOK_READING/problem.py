import numpy as np
T = int(input())
for t in range(1,T+1):
    line = [int(x) for x in input().split(" ")]
    N, M, Q = line[0], line[1], line[2]
    P = [int(x) for x in input().split()]
    R = [int(x) for x in input().split()]
    # print(bad_pages, read_r)
    book = np.ones(N+1)
    for m in range(M):
        book[P[m]] = 0
    y = 0
    read_seen = {}

    for q in range(Q):
        read = 0
        if R[q] in read_seen:
            y += read_seen[R[q]]
        else:
            for i in range(R[q], N+1, R[q]):
                read += book[i]
            y += int(read)
            read_seen[R[q]] = int(read)
    print("Case #{}: {}".format(t, y))







