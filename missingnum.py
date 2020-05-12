a = input()
b =  list(a)
s = list(map(int,b))
c = 0
nc = 0
for i,j in zip(b,b[1::]):
    if int(j) - int(i) == 1:
        c += 1
    else:
        break
if c > 2:
    d = list(range(s[0],len(s)+2))
    for i in d:
        if i not in s:
            nc += 1
    if nc > 1:
        print('-1')
    else:
        print(i)       
    
else:
    c = []
    e = []
    o = []
    d = []
    for i in range(len(b)):
        if i % 2 == 0:
            e.append(a[i])
        else:
            o.append(a[i])

    for i,j in zip(e,o):
        i = str(i)+str(j)
        c.append(int(i))
        
    s = c[0]
    e = c[len(c)-1]

    for i in range(s,e+1):
        d.append(i)
    
    #print(d)
    for i in d:
        if i not in c:
            nc += 1
    if nc > 1:
        print('-1')
    else:
        print(i)
