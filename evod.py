a = input()
b = []

for i in a:
    if i.isdigit():
        b.append(i)
        
c = list(set(b))

d = list(map(int,c))

e = []
f = []

for i in d:
    if i % 2 == 0:
        e.append(i)
m = min(e)
for i in d:
    if i != m:
        f.append(i)
j = sorted(f,reverse = True)
j.append(m)
f = list(map(str,j))
print(''.join(f))
