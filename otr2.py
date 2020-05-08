
a = []
n = int(input())
for i in range(1,n+1):
        x,y = map(int, input().split())
        a.append([x,y])
def getKey(item):
    return item[1]
a.sort(key = getKey)  

print(a)

dotes = []
while(len(a) != 0):
	if len(a) == 1:
		dotes.append(a[0][1])
		a.remove(a[0])
		break
	if a[0][1] >= a[1][0]:                  
		a.remove(a[1])
	else:
		dotes.append(a[0][1])
		a.remove(a[0])



print(len(dotes))
for i in dotes:
   print(i, end = ' ')
