password = input()
c = 0
d = ''
u = ''
l = ''
special_characters = "!@#$%^&*()-+"
s = ''

    
for i in password:
    if i.isdigit():
        d += i
    if i.isupper():
        u += i
    if i.islower():
        l += i
    if i in special_characters:
        s += i
if len(d) == 0:
    c += 1
if len(u) == 0:
    c += 1
if len(l) == 0:
    c += 1
if len(s) == 0:
    c += 1
#print(c)
if len(password) <= c:
    c =c + len(password)
    c += 6-c
    c = c - len(password)
elif len(password)+c < 6:
    c += len(password)-c


print(c)

