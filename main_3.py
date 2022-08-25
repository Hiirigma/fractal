n, m, a = list(map(int, input().split()))
my_list = []
sm = 0
x = 0
y = 0
b = 1
c = 1
d = 1
e = 1
for g in range(n):
    my_list.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if my_list[i][j] == a:
            x = i
            y = j
if y == 0:
    if x == 0:
        b = my_list[x + 1][y + 1]
    elif x == m - 1:
        b = my_list[x - 1][y + 1]
    else:
        if x + 1 < m - 1:
            b = my_list[x + 1][y + 1]
        c = my_list[x - 1][y + 1]
# fix (test10)
elif x == 0:
    if y + 1 < n and x + 1 < m - 1:
        c = my_list[x + 1][y + 1]
    if x + 1 < m - 1 and y != 0:
        d = my_list[x + 1][y - 1]
# -------------------------------
elif y == n - 1:
    if x == 0:
        b = my_list[x + 1][y - 1]
    elif x == m - 1:
        b = my_list[x - 1][y - 1]
    else:
        # Fix (test5)
        # -----------------------
        if x + 1 < m - 1:
            b = my_list[x + 1][y - 1]
        # -----------------------
        c = my_list[x - 1][y - 1]
        # Fix (test3)
        # -----------------------
        if x + 1 < m - 1:
            d = my_list[x + 1][y + 1]
        e = my_list[x - 1][y + 1]
        # -----------------------
else:
    if x != 0 and x != m - 1:
        # Fix (test12)
        if x + 1 < m - 1 and y + 1 < n:
            b = my_list[x + 1][y + 1]
        if y + 1 < n:
            c = my_list[x - 1][y + 1]
        # Fix (test12)
        if x + 1 < m - 1:
            d = my_list[x + 1][y - 1]
        e = my_list[x - 1][y - 1]
print(b * c * d * e)

"""
test 1
16
2 2 10
10 11
13 16

test2
60
3 4 10
11 12 30 4
10 20 30 1
60 5 8 7

test3
1680
3 4 30
11 12 10 4
10 20 30 1
60 5 8 7

test4
20
3 4 10
11 12 10 4
30 20 30 1
60 5 8 7

test5
20
3 4 8
11 12 10 4
30 20 30 1
60 5 8 7

test6
52800
3 4 20
11 12 10 4
30 20 30 1
60 5 8 7

test7
20
3 4 11
11 12 10 4
30 20 30 1
60 5 8 7

test8
60
3 4 30
11 12 10 4
30 20 20 1
60 5 8 7

test9
20
3 4 60
11 12 10 4
30 20 20 1
60 5 8 7

test10
600
3 4 12
11 12 10 4
30 20 20 1
60 5 8 7

test11
52800
3 4 20
11 12 10 4
30 20 10 1
60 5 8 7

test12
300
3 4 5
11 12 10 4
30 20 10 1
60 5 8 7

test13
20
3 4 10
11 12 10 4
30 20 20 1
60 5 8 7

test14
1680
3 4 20
11 12 10 4
30 30 20 1
60 5 8 7

test15
30
3 4 8
11 12 10 4
30 30 20 1
60 5 8 7

test16
20
3 4 4
11 12 10 4
30 30 20 1
60 5 8 7

test17
80
3 4 1
11 12 10 4
30 30 20 1
60 5 8 7

test18
20
3 4 7
11 12 10 4
30 50 20 1
60 5 8 7

"""