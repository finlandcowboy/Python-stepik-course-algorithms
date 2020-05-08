import heapq, sys

def insert(self,priority):

    heapq.heappush(self, -priority)

def extract_max(self):
    return -heapq.heappop(self)


heap = []
heapq.heapify(heap)
x = int(input())
a = list(map(lambda _: input(),range(x)))

for i in range(len(a)):
    if a[i].startswith('Insert'):
        command, num = a[i].split()
        heapq.heappush(heap,num * -1)
    else:
        print(heapq.heappop(heap) * -1)



