a = input()
b = input()

for i,j in zip(a,a[1::]):
    if i == '-' and j == '-' and a.count('+')<b.count('+'):
        print('yes')
        break
    elif len(a) < len(b):
        print('no')
        break
    elif len(a) == len(b):
        print('yes')
        break
    
