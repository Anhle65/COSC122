"""
File = patient_queue.py
Author = Anh Le

Maintain a patient queue that sorts patients based on the diseases
they have been diagnosed with, and the time since the diagnosis.
"""

from classes3 import PriorityQueue, Patient


class PatientQueueHeap(PriorityQueue):
    """Implement a queue structure using a 0-indexed Heap.
    This particular type of queue is designed to hold patient information.
    """

    def __init__(self, start_data=None, fast=False):
        """Creates the patient queue."""
        if start_data is None:
            start_data = []
        self.comparisons = 0
        self.data = []
        if fast:
            self._fast_heapify(start_data)
        else:
            self._heapify(start_data)

    def _swap(self, i, j):
        """Swap the patients at positions i and j."""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _parent_index(self, index):
        """Determine the parent index of the current index.
        For a binary heap that is zero-indexed, this is
        p = (i - 1) // 2
        """
        return (index - 1) // 2

    def _child_indices(self, index):
        """Calculate the child indices for the current index.
        For a binary heap that is zero-indexed, this is
        c1 = 2*i + 1
        c2 = 2*i + 2
        """
        return [2 * index + delta for delta in range(1, 2 + 1)]

    def _max_child_priority_index(self, child_indices):
        """Find the child among the given indices that has the highest priority.
        If an index is not valid, do not consider it. If none are valid, then
        return None. Assumes the child_indices are in order.
        """
        max_index = None
        for index in child_indices:
            if index >= len(self.data):
                break  # No more valid children
            if max_index is None:  # This is the first child, it's valid, so use it
                max_index = index
            else:
                self.comparisons += 1  # Don't worry, we do the comparison counting here
                if self.data[index].priority > self.data[max_index].priority:
                    max_index = index
        return max_index

    def _sift_up(self, index):
        """Move the patient at the given index into the correct location
        further up in the heap by swapping with its parents if appropriate.
        """
        # ---start student section---
        # parent = self._parent_index(index)
        while (index - 1) // 2 >= 0:
            parent = self._parent_index(index)
            self.comparisons += 1
            if self.data[index].priority > self.data[parent].priority:
                self._swap(index, parent)
            else:
                break
            index = parent 
        # ===end student section===

    def _sift_down(self, index):
        """Move the patient at the given index into the correct location
        further down in the heap by swapping with its children if appropriate.
        """
        # ---start student section---
        while index*2 <= len(self.data):
            data = self._child_indices(index)
            mc = self._max_child_priority_index(data)
            if mc is None:
                break
            self.comparisons += 1
            if self.data[index].priority < self.data[mc].priority:
                self._swap(index, mc)
            index = mc

        # ===end student section===

    def _heapify(self, data):
        """Turn the existing data into a heap in O(n log n) time."""
        for patient in data:
            self.enqueue(patient)

    def _fast_heapify(self, data):
        """Turn the existing data into a heap in O(n) time.
        """
        # ---start student section---
        i = len(data)//2
        self.data += data[:]
        while i >= 0:
            self._sift_down(i)
            i = i - 1
        # ===end student section===

    def enqueue(self, patient):
        """Add a patient to the queue.
        """
        # We first make sure that we're only including Patients
        assert isinstance(patient, Patient)
        # ---start student section---
        self.data.append(patient)
        if len(self.data) > 1:
            self._sift_up(len(self.data)-1)
        # ===end student section===

    def dequeue(self):
        """Take a patient off the queue and return the Patient object.
        """
        # ---start student section---
        if len(self.data) == 0:
            raise IndexError ("There no more patient in queue")
        else:
            self._swap(0, len(self.data)-1)
            get_off = self.data.pop()
            if len(self.data) > 2:
                self._sift_down(0)
            return get_off
        # ===end student section===




# if __name__ == "__main__":
    # put your own simple tests here
    # you don't need to submit this code
    # print("Add some tests here...")
    # patient2 = Patient("Toy", 100, 20)
    # patient = Patient("Nancy Toney", 50, 31)
    # patient3 = Patient("Nancy Toney", 50, 30)
    # patient1 = Patient("Toney", 10, 20)
    # patient0 = Patient("Tgh", 20, 20)
    # patient4 = Patient("new", 10, 10)
    # patient5 = Patient("Tgh", 15, 15)
    # patient6 = Patient("Tgh", 17, 18)
    # my_heap = PatientQueueHeap(fast=True)
    # print(my_heap)
    # print(my_heap.comparisons)
    # my_heap.enqueue(patient)
    # print(my_heap)
    # # my_heap.enqueue(patient1)
    # my_heap.enqueue(patient3)
    # print(my_heap)
    # print(my_heap.comparisons)
    # # my_heap.enqueue(patient2)
    # # my_heap.enqueue(patient0)
    # # my_heap.enqueue(patient4)
    # # my_heap.enqueue(patient5)
    # # my_heap.enqueue(patient6)
    # print(my_heap)
    # print(my_heap.dequeue())
    # print(my_heap.comparisons)
    # print(my_heap)
    # print(my_heap.comparisons)

    # print(my_heap.dequeue())
    # print(my_heap.comparisons)

    # print(my_heap)
# from utilities import verify_heapness, read_test_data
# patients, _ = read_test_data("student_files/test_data/test_data-5-5-0.txt")
# my_heap = PatientQueueHeap(start_data=patients, fast=True)
# print(my_heap)
# print(verify_heapness(my_heap))
def _fast_heapify(self, data):
        """Turn the existing data into a heap in O(n) time.
        """
        # ---start student section---
        i = len(data)//2
        self.data += data[:]
        while i >= 0:
            self._sift_down(i)
            i = i - 1
        return data
print(_fast_heapify([None, 64, 44, 36, 68, 12]))
