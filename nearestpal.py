def pal(n):
	s = str(n)
	n = len(s) // 2
	ch = s[n] if len(s) % 2 else ''
	s1 = s[:n]
	return int(s1 + ch + s1[-1::-1])
	
n = int(input())
print(pal(n))
        
        
    
