a = int(input())
b = input()
if a == 1:
    print(b)

l = len(b)

ar = ['' for i in range(l)]

r = 0

for i in range(l):
    ar[r] += b[i]
    
    if r == a-1:
        down = False
    elif r == 0:
        down = True
        
    if down:
        r += 1
    else:
        r -= 1
        
for i in range(a):
    print(ar[i],end = '')
