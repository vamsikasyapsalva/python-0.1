def isValid(s):
    s = list(s)
    c = []
    k = []
    r = 0
    for i in s:
        c.append(s.count(i))
    d = dict(dict(zip(s,c)))
    #d = dict(sorted(d,))
    #print(d)
    for i in d.values():
        k.append(i)
    #print(k)
    f = set(k)
    if len(k) == 1:
        return 'YES'
    elif len(k) > 1:
        if k.count(max(k)) == 1 and k.count(min(k)) == 1 :
            return 'NO'
        elif k.count(max(k)) == 1:
            return 'YES'
        elif k.count(min(k)) == 1:
            return 'YES'
        elif k.count(min(k)) > 1 or k.count(max(k)) > 1:
            return 'NO'
        
   
        
