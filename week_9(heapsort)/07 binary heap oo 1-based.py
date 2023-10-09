#Binary min-heap that stores the root at location 1 of a list

class BinaryMinHeap:
    def __init__(self):
        self._heap = [None] # location 0 is unused
        self.current_size = 0
        
    def _perc_up(self, cur_idx):
        while cur_idx // 2 >= 1:  # has a parent
            parent_idx = cur_idx // 2
            if self._heap[cur_idx] < self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx],
                )
            cur_idx = parent_idx        
            
            
    def _perc_down(self, cur_idx):
        while 2 * cur_idx <= self.current_size: # has at least one child
            min_child_idx = self._get_min_child(cur_idx)
            if self._heap[cur_idx] > self._heap[min_child_idx]:
                self._heap[cur_idx], self._heap[min_child_idx] = (
                    self._heap[min_child_idx],
                    self._heap[cur_idx],
                )
            else:
                return
            cur_idx = min_child_idx
    
    def _get_min_child(self, parent_idx):
        if 2 * parent_idx + 1 > self.current_size: # only one child
            return 2 * parent_idx
        if self._heap[2 * parent_idx] < self._heap[2 * parent_idx + 1]:
            return 2 * parent_idx
        return 2 * parent_idx + 1            
    
    def insert(self, item):
        self._heap.append(item)
        self.current_size += 1
        self._perc_up(self.current_size)
            
    def delete(self):
        self._heap[1], self._heap[-1] = self._heap[-1], self._heap[1]
        result = self._heap.pop()
        self.current_size -= 1
        self._perc_down(1)
        return result    
    
    def is_empty(self):
         return self.current_size == 0
    
    def heapify(self, not_a_heap):
        self._heap = [None] + not_a_heap[:] # start data at location 1
        self.current_size = len(not_a_heap)
        cur_idx = self.current_size // 2    # fast heapify
        while cur_idx >= 1:
            self._perc_down(cur_idx)
            cur_idx = cur_idx - 1
            
pq = BinaryMinHeap()
pq.insert(4)
pq.insert(6)
pq.insert(2)
pq.insert(9)
pq.insert(3)
print(pq._heap)
#print(pq.delete())
#print(pq.delete())
#print(pq.delete())
#print(pq.delete())
#print(pq.delete())

#big = BinaryMinHeap()
#alist = [4,3,7,93,2,6,9,12,43,1]
#big.heapify(alist)
#while not big.is_empty():
    #print(big.delete())
