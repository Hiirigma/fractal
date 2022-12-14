n, m = map(int, input().split())

lab = []
for i in range(n):
    vr_ls = [int(s) for s in input().split()]
    lab.append(vr_ls)

a, b = map(int, input().split())

# check start and end positions
if lab[0][0] == 1:
    print(-1)
    exit(0)

if lab[a][b] == 1:
    print(-1)
    exit(0)

for i in range(len(lab)):
    for j in range(len(lab[i])):
        if lab[i][j] == 0:
            lab[i][j] = -1
        elif lab[i][j] == 1:
            lab[i][j] = -2

lab[0][0] = 0

t = [(0, 0)]

while len(t) != 0:
    t_vr = []
    for koo in t:
        i, j = koo[0], koo[1]
        count = lab[i][j] + 1

        # bug fix - change elif to if
        # up move
        if i > 0 and lab[i - 1][j] == -1:
            lab[i - 1][j] = count
            t_vr.append((i - 1, j))
        # down move
        if i < n - 1 and lab[i + 1][j] == -1:
            lab[i + 1][j] = count
            t_vr.append((i + 1, j))
        # left move
        if j > 0 and lab[i][j - 1] == -1:
            lab[i][j - 1] = count
            t_vr.append((i, j - 1))
        # right move
        if j < m - 1 and lab[i][j + 1] == -1:
            lab[i][j + 1] = count
            t_vr.append((i, j + 1))

    t = t_vr

print(lab[a][b])

"""
8 
4 4
0 0 0 1
1 1 0 1
0 1 0 1
0 0 0 0
2 0

1
6 6
0 1 0 0 1 1
0 0 0 1 1 1
0 0 0 1 1 0
1 0 0 1 1 1
0 1 0 1 0 0
0 1 1 0 0 0
1 0

-1
5 4
0 0 1 1
1 1 0 1
0 0 1 0
0 0 0 1
1 1 0 0
1 2

-1
5 4
0 0 1 1
1 1 0 1
0 0 1 0
0 0 0 1
1 1 0 0
1 2

-1
5 4
0 0 1 1
1 1 0 1
0 0 1 0
0 0 0 1
1 1 0 0
2 2

7
5 4
0 0 1 1
0 1 0 1
0 0 1 0
0 0 0 1
1 1 0 0
4 3

6
5 4
0 0 1 1
0 1 0 1
0 0 1 0
0 0 0 1
1 1 0 0
4 2

11
5 4
0 0 1 0
0 1 0 0
0 0 1 0
0 0 1 0
1 0 0 0
0 3

16
6 5
0 0 1 0 0
0 1 0 0 1
0 0 1 0 0
0 0 1 1 0
1 0 1 0 0
1 0 0 0 1
0 4

1
2 2
0 0
0 1
0 1

1
2 2
0 0
0 1
1 0

-1
2 2
1 0
0 1
1 1

"""