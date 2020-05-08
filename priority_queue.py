import heapq,sys

class PriorityQueueStandardLibrary:
    queue = []
    heapq.heapify(queue)

    def insert(self, priority):
        """Time complexity: O(log(n)), where n = len(self.queue)"""
        heapq.heappush(self.queue, -priority)  # (-priority) because it's a min heap

    def extract_max(self):
        """Time complexity: O(log(n)), where n = len(self.queue)"""
        return -heapq.heappop(self.queue)  # minus because every heap element is a negative number

priority_queue = PriorityQueueStandardLibrary()

n_ = input()
for line in sys.stdin.readlines():
    if line.startswith('Insert'):
        _command, n = line.split()
        priority_queue.insert(int(n))
    else:
        print(priority_queue.extract_max())
