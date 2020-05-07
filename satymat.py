
def check(x):
    dig, s = 0, x
    while(s>0):
        dig += s%10
        s = s//10
    if(x%dig == 0):
        return True
    return False

l = input().split()
r,c = int(l[0]), int(l[1])
l = []
for i in range(r):
    l.append( [ int(x) for x in input().split()])
for i in range(r-1):
    for j in range(c-1):
        if( check(l[i][j]) and check(l[i+1][j]) and check(l[i][j+1]) and check(l[i+1][j+1]) ):
            print(l[i][j],l[i][j+1], sep=" ")
            print(l[i+1][j],l[i+1][j+1], sep=" ")
