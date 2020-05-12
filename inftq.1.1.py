a = 'google'
b = list(sorted(set(a),key = a.index))
print(''.join(b[::-1]))
