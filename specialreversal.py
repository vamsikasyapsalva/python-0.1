a = input()
a = list(a)
b = []
k = []

for i in a:
    if i.isalpha():
        b.append(i)
        k.append(a.index(i))
        
b = b[::-1]

for i in a:
    if i.isalpha() == False:
        b.insert(a.index(i),i)
        
print(''.join(b))
