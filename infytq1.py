a = 'google'
#output : 'elog'
a = list(sorted(dict.fromkeys(a),key = a.index))
print(''.join(a[::-1]))
