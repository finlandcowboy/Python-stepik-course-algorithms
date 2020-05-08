n = int(input())
coordinates = dict([input('Введите ключ и значение через пробел:').split() for _ in range(n)])
a = list(coordinates.items())
a.sort(key = lambda i : i[1])
k = 0
#while(k < n):
for i in range(n):
	print(a[i][1])