a = input()
c = 0
e = []
o = []
r = []
k = []
s = 0
for i in a:
    if i.isdigit() == True or i.isalpha() == True:
        continue
    else:
        c += 1
for i in a:
    if i.isdigit():
        i = int(i)
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)
print(e)
print(o)

if c % 2 == 0:
    if len(o) > len(e):
        for i,j in zip(e,o):
            r.append(i)
            r.append(j)
        k = o[len(e):]
        for i in k:
            r.append(i)
        
        r = list(map(str,r))
       
    elif len(e) > len(o):
        for i,j in zip(e,o):
            r.append(i)
            r.append(j)
        k = e[len(o):]
        for i in k:
            r.append(i)
        r = list(map(str,r))
    elif len(o) == len(e):
        for i,j in zip(e,o):
            r.append(i)
            r.append(j)
        r = list(map(str,r))
if c % 2 != 0:
    if len(o) > len(e):
        for i,j in zip(o,e):
            r.append(i)
            r.append(j)
        k = o[len(e):]
        for i in k:
            r.append(i)
        r = list(map(str,r))
    elif len(e) > len(o):
        for i,j in zip(o,e):
            r.append(i)
            r.append(j)
        k = e[len(o):]
        for i in k:
            r.append(i)
        r = list(map(str,r))
    elif len(o) == len(e):
        for i,j in zip(o,e):
            r.append(i)
            r.append(j)
        r = list(map(str,r))
print(''.join(r))
