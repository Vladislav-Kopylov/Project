Q = int(input())
KC = []
for k in range(Q):
    KC.append(list(map(int, input().split())))
n = int(100000)
lst = [2]
for i in range(3, n + 1, 2):
    if (i > 10) and (i % 10 == 5):
        continue
    for j in lst:
        if j * j - 1 > i:
            lst.append(i)
            break
        if i % j == 0:
            break
    else:
        lst.append(i)
for i in range(Q):
    k = KC[i][0]
    ct = KC[i][1] - 1
    o = ct
    z = 0
    ctleft = lst[z]
    ctright = lst[o]
    while ctright - ctleft != k:
        if ctright - ctleft > k:
            print(-1)
            break
        elif ctright - ctleft == k:
            print(ctleft)
            break
        while ctright - ctleft != k and ctright + 1 != lst[o+1]:
            ctright += 1
            if ctright - ctleft == k:
                print(ctleft)
                break

        if ctleft == lst[z]:
            ctleft -= 1
            if ctright - ctleft == k:
                print(ctleft)
                break
            continue
        o += 1
        z += 1
        ctright = lst[o]
        ctleft = lst[z]
        if lst[o] == lst[-1]:
           # print('finish')
            break
