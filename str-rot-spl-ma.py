a = input()
a = a.split(',')
print(a)
al = []
n = []
alp = []
su = 0
sq = []
for i in a:
    i = i.split(':')
    al.append(i)
    
print(al)
sq = []

for i in al:
    for j in i:
        if j.isalpha():
            n.append(j)
        elif j.isdigit():
            alp.append(j)
            
print(n)
m = list(map(int,alp))
print(m)
def sq(a):
    su = 0
    for i in str(a):
        su +=int(i)*int(i)
    return su
f = list(map(sq,m))
print(f)
for i,j in zip(f,n):
    if i % 2 == 0:
        print(j[-1]+j[0:len(j)-1])
        
    elif i % 2 != 0:
        print(j[2:len(j)]+j[0:2])
