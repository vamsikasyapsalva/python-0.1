def fun(a):
    if a == a[::-1]:
        print(a)
    else:
        a = list(a)
        a.remove(a[0])
        a = ''.join(a)
        fun(a)

a = input()
fun(a)
