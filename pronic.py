a = input()
d = int(a)
b = list(a)
c = list(map(int,b))
s = []

for i,j in zip(c[::],c[1::]):
    k = i*j
    if str(k) in str(d):
        s.append(k)
if len(s) != 0:
    print(s)
else:
    print('-1')
        
