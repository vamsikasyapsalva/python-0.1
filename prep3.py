a = input().split()
s = a[0]
ss = a[1]

for i in s:
    if ss in s:
        print('YES')
        break
    else:
        print('NO')
        break
