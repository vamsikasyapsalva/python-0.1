a = input()
b = []
ind = []
for i in a:
    if  i.isalpha():
        b.append(i)
    else:
        ind.append(a.index(i))
        
c = list(reversed(b))

for i in ind:
    c.insert(i,a[i])
    
print(''.join(c))
    
