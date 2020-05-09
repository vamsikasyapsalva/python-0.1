a = 'aaabaa'
a = list(a)
c = 0
d = 0
for i in a:
    if i == 'a':
        c += 1
    else:
        d += 1
if c > len(a)//2:
    print(len(a))
else:
    for i in a:
        if i != 'a':
            a.remove(i)
            d -= 1
            if c > d:
                break
    print(len(a)-1)
