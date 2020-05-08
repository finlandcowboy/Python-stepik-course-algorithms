n = int(input())
coordinates = dict([input('Введите ключ и значение через пробел:').split() for _ in range(n)])
a = list(coordinates.items())
dotes = []
a.sort(key = lambda i : i[1])
while len(a) != 0 :
    for j in range(len(a)- 2): 
	    if int(a[0][1]) >= int(a[j][0]): print(a[0][1] + "  " + a[j][0])
		
    dotes.append(a[0][1])
    print(a)
    a.remove(a[0])
   
    print(dotes)
    print("---------")
    
print(len(dotes))
print(dotes)
