n = int(input())
coordinates = dict([input().split() for _ in range(n)])
a = list(coordinates.items())
dotes = []
a.sort(key = lambda i : i[1])
for i in a:
    for j in a:
        print("j =",j, " i=",i)
        print("До ", a)
        if a.index(i) < a.index(j):
            if i[1] >= j[0]: 
                a.remove(j)
                print("++++++++")
        	
        print("После ",a)	
    dotes.append(i[1])
    print("DOTES == ", dotes)

print(len(dotes))
for i in range(len(dotes)):
    print(dotes[i])
