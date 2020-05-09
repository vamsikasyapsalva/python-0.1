def fun(a):
    c = -1
    c += 1
    if a == a[::-1]:
        print(c)
    else:
        for i,j in zip(a,a[::-1]):
            if i != j:
                c += 1
        print(c)
    
a = input()
fun(a)
