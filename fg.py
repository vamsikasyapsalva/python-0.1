a = list(map(int,input().split(',')))
c = []

for i in a:
    s = 1
    for j in range(2,i + 1):
        if i % j == 0:
            s += j
    if s in a:
        c.append(i)
        
if len(c) != 0:
    print(c)
else:
    print('-1')
