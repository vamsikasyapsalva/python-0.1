a = int(input())
c = []
b = list(range(a,0,-1))
for i in b:
    i = list(str(i))
    for j,k in zip(i,i[1::]):
        if j < k:
            c.append(''.join(i))
            
print(max(c))
            


    
