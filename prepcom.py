import itertools

a = input()
c = 'CODE'
c = list(c)
d = []
if len(a) % 4 ==0:
    b = len(a) // 4
    s = itertools.permutations(a,4)
    s = list(s)
    for i in s:
        i = list(i)
        d.append(i)
        #print(d)
    for i in d:
        if i == c:
            print('0')
            break
        else:
            print(b)
            break
    
